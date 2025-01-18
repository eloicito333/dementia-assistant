from datetime import datetime, timedelta
from threading import Thread
from time import sleep

from api_helper import api_helper
from server import socket


def parse_iso_datetime(dt_str):
    """
    Attempt to parse a date/time string in ISO 8601 format,
    e.g. 2024-10-31T15:00:00.000Z or 2024-10-31T15:00:00Z.
    Returns a datetime object or None if parsing fails.
    """
    if not dt_str:
        return None
    
    # Remove trailing 'Z' if present, since datetime.fromisoformat
    # in Python < 3.11 doesn't handle 'Z' suffix for UTC
    # (Python 3.11+ does handle 'Z', but we'll keep it for safety)
    dt_str = dt_str.rstrip('Z')
    
    try:
        # fromisoformat can parse 2024-10-31T15:00:00.000
        # if you have more specialized cases (e.g. offset times),
        # consider dateutil.parser.isoparse instead.
        return datetime.fromisoformat(dt_str)
    except ValueError:
        return None


def parse_time_string(time_str):
    """
    Handle strings like "HH:MM", "HH:MM:SS", possibly with trailing 'Z'.
    Return a time object or None on failure.
    """
    if not time_str:
        return None

    # Remove trailing 'Z', if present
    time_str = time_str.rstrip('Z')

    # If it's "HH:MM", append ":00"
    if time_str.count(':') == 1:
        time_str += ":00"
    
    try:
        return datetime.strptime(time_str, "%H:%M:%S").time()
    except ValueError:
        return None


class Reminder:
    def __init__(
        self,
        frequency,
        title,
        description,
        date=None,
        starts=None,
        expires=None,
        weekdays=None,
        doneDuration=None,
        tellBeforeDuration=None,
        nextReminding=None,
        remembering=False
    ):
        
        self.remembering = remembering

        
        self.frequency = frequency
        self.title = title
        self.description = description
        
        # Convert these server-sent strings into datetime objects
        self.date = parse_iso_datetime(date) if date else None
        self.starts = parse_iso_datetime(starts) if starts else None
        self.expires = parse_iso_datetime(expires) if expires else None
        
        self.weekdays = weekdays  # List with times or False
        self.doneDuration = doneDuration  # Not changed—depends on your usage
        
        # Convert "HH:MM:SS" or "HH:MM" to a number of seconds
        if tellBeforeDuration:
            self.tellBeforeDuration = timedelta(seconds=self.time_str_to_seconds(tellBeforeDuration))
        else:
            self.tellBeforeDuration = None
        
        # Convert nextReminding from server string to datetime, if present
        self.nextReminding = parse_iso_datetime(nextReminding) if nextReminding else None

    def to_dict(self):
        return {
            "frequency": self.frequency,
            "title": self.title,
            "description": self.description,
            "date": self.date.isoformat() if self.date else None,
            "starts": self.starts.isoformat() if self.starts else None,
            "expires": self.expires.isoformat() if self.expires else None,
            "weekdays": self.weekdays,
            "doneDuration": self.doneDuration,
            "tellBeforeDuration": self.tellBeforeDuration.total_seconds() if self.tellBeforeDuration else None,
            "nextReminding": self.nextReminding.isoformat() if self.nextReminding else None,
        }

    def time_str_to_seconds(self, time_str):
        """
        Convert "HH:MM" or "HH:MM:SS" (possibly with trailing 'Z') to integer seconds.
        """
        # Remove trailing 'Z'
        time_str = time_str.rstrip('Z')
        # If "HH:MM" => "HH:MM:00"
        if time_str.count(':') == 1:
            time_str += ":00"
        
        h, m, s = map(int, time_str.split(':'))
        return h * 3600 + m * 60 + s

    def getNextRemindingTime(self):
        """
        Calculate (and return) the next reminding time as a datetime object.
        If self.nextReminding is already set, just return it.
        """
        if self.nextReminding: 
            return self.nextReminding

        # Single (once) reminder
        if self.frequency == "once":
            # nextReminding is (date - tellBeforeDuration) if tellBeforeDuration is set, else date
            if self.date:
                self.nextReminding = (self.date - self.tellBeforeDuration) if self.tellBeforeDuration else self.date
            return self.nextReminding

        # Recurrent (multiple) reminders
        if self.frequency == "multiple" and self.weekdays:
            now = datetime.now()
            i = 0
            # Check up to 7 days from now to find the next valid day/time
            while i < 14:  # up to 2 weeks if needed, just a safe margin
                day_index = (now.weekday() + i) % 7
                day_schedule = self.weekdays[day_index]
                
                if day_schedule and day_schedule != False:
                    # Sort times in ascending order
                    sorted_times = sorted(day_schedule)
                    
                    for time_str in sorted_times:
                        parsed_time = parse_time_string(time_str)
                        if not parsed_time:
                            # If time string is invalid, skip
                            continue
                        
                        # Build a candidate datetime for day_index, using the time
                        candidate = (now + timedelta(days=i)).replace(
                            hour=parsed_time.hour,
                            minute=parsed_time.minute,
                            second=parsed_time.second,
                            microsecond=0
                        )
                        # Check that candidate is in the future and after starts (if set)
                        if candidate > now and (not self.starts or candidate > self.starts):
                            # Subtract tellBeforeDuration if present
                            if self.tellBeforeDuration:
                                candidate -= self.tellBeforeDuration
                            self.nextReminding = candidate
                            return self.nextReminding
                i += 1

        return None  # If nothing found, returns None


class RemindersManager:
    def __init__(self, assistant):
        self.reminders = []
        self.assistant = assistant
        self.updateReminders()

    def updateReminders(self):
        # Load reminders from your DB via the api_helper
        reminders = api_helper.reminders_db.get_all_reminders()

        print("REMINDERS FETCHED: ", reminders)

        self.reminders.clear()  # Reset the list before re-populating

        for reminder in reminders:
            frequency = reminder.get('frequency')
            title = reminder.get("title")
            description = reminder.get("description")
            date = reminder.get("date")  # e.g. "2024-10-31T15:00:00.000Z"
            starts = reminder.get("starts")
            expires = reminder.get("expires")
            weekdays = reminder.get("weekdays")
            doneDuration = reminder.get("doneDuration")
            tellBefore = reminder.get("tellBefore")
            nextReminding = reminder.get("nextReminding")

            self.reminders.append(Reminder(
                frequency=frequency,
                title=title,
                description=description,
                date=date,
                starts=starts,
                expires=expires,
                weekdays=weekdays,
                doneDuration=doneDuration,
                tellBeforeDuration=tellBefore,
                nextReminding=nextReminding,
                remembering=False
            ))

        # Force each reminder to compute its next reminding time once
        for reminder_obj in self.reminders:
            reminder_obj.getNextRemindingTime()

    def _run(self):
        # Let the DB -> Python "refresh" happen by linking your update function
        api_helper.reminders_db.refresh_reminders_fn = self.updateReminders

        while True:
            now = datetime.now()
            for reminder in self.reminders:
                next_reminding = reminder.getNextRemindingTime()

                if next_reminding and now >= next_reminding:
                    # It's time to remind
                    if not reminder.remembering:
                        print("Its time to remind: ", reminder)
                        self.assistant.reminder_time(reminder.to_dict())
                    reminder.remembering = True

                    # Update nextReminding depending on its frequency
                    if reminder.frequency == "once":
                        # One-time reminder => mark it done
                        reminder.nextReminding = None
                    elif reminder.frequency == "multiple":
                        # Recurrent => compute the next occurrence
                        reminder.nextReminding = None
                        reminder.getNextRemindingTime()

            # Sleep a bit to avoid busy waiting
            sleep(1)
    
    def run_on_socket_start(self):
        thread = Thread(name="RemindersRuntime", target=self._run, daemon=True)
        thread.start()
        return thread

    def run(self):
        socket.run_reminders_setup = self.run_on_socket_start