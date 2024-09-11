import queue
import numpy as np
from threading import Thread


from  program_settings import verbose, no_delete
from stream_constants import SampleRate, BlockSize

from client import socket

class AudioPlayer:
    def __init__(self):

        self.stop_flag=False

        self.output_queue=queue.Queue()
        self.output_buffer=np.zeros((int(SampleRate * BlockSize / 1000), 1), dtype=np.float32)

        def outdata(data):
            print("received outdata")
            block = data["outdata"]
            
            self.output_queue.put(block)

        socket.on("outdata", outdata)


    def _stop(self):
        self.stop_flag = True
        #clearing the queue
        with self.output_queue.mutex:
            self.output_queue.queue.clear()

    def stop(self):
        thread=Thread(name="AIAssistant_stop_playing", target=self._stop)
        thread.start()
        return thread