<p align="center">
  <img src="dementia-assistant.png" width="60%" alt="DEMENTIA-ASSISTANT-logo">
</p>
<p align="center">
    <h1 align="center">DEMENTIA-ASSISTANT</h1>
</p>
<p align="center">
    <em>Empowering Minds, Easing Memories-Your Real-time Ally in Early Dementia Care</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/License-Modifiev d%20Creative%20Commons?style=flat&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/eloicito333/dementia-assistant?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/eloicito333/dementia-assistant?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/eloicito333/dementia-assistant?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Built with the tools and technologies:</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=flat&logo=JavaScript&logoColor=black" alt="JavaScript">
	<img src="https://img.shields.io/badge/Pydantic-E92063.svg?style=flat&logo=Pydantic&logoColor=white" alt="Pydantic">
	<img src="https://img.shields.io/badge/Nodemon-76D04B.svg?style=flat&logo=Nodemon&logoColor=white" alt="Nodemon">
	<img src="https://img.shields.io/badge/MongoDB-47A248.svg?style=flat&logo=MongoDB&logoColor=white" alt="MongoDB">
	<br>
	<img src="https://img.shields.io/badge/OpenAI-412991.svg?style=flat&logo=OpenAI&logoColor=white" alt="OpenAI">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/NumPy-013243.svg?style=flat&logo=NumPy&logoColor=white" alt="NumPy">
	<img src="https://img.shields.io/badge/JSON-000000.svg?style=flat&logo=JSON&logoColor=white" alt="JSON">
	<img src="https://img.shields.io/badge/Express-000000.svg?style=flat&logo=Express&logoColor=white" alt="Express">
</p>

<br>

##### 🔗 Table of Contents

- [📍 Overview](#-overview)
- [👾 Features](#-features)
- [📂 Repository Structure](#-repository-structure)
- [🧩 Modules](#-modules)
- [🚀 Getting Started](#-getting-started)
    - [🔖 Prerequisites](#-prerequisites)
    - [📦 Installation](#-installation)
    - [🤖 Usage](#-usage)
    - [🧪 Tests](#-tests)
- [📌 Project Roadmap](#-project-roadmap)
- [🤝 Contributing](#-contributing)
- [🎗 License](#-license)
- [🙌 Acknowledgments](#-acknowledgments)

---

## 📍 Overview

The open-source project, dementia-assistant, is ingeniously developed to lend an assistive hand to those suffering from dementia by leveraging real-time handling and transcription of audio data. The software project is primarily kicked off by main.py, which is the linchpin, orchestrating various client-side functionalities such as initializing voice assistant, audio player, and transcription handler, and triggering audio recording and transcribing processes, among other tasks. The heart of real-time operations lies in stream_handler.py, adept at managing and processing audio data with the use of several critical libraries. Further, it prepares the audio data for transcribing by interacting with transcriber.py. Furthermore, openai_client.py augments the functionality by providing an interface to OpenAI GPT-3, thereby enabling user interaction with the model for question-answering and conversation. The unique value proposition of the software project lies in its real-time assistance, providing significant help to dementia patients, thereby enhancing their quality of life.

---

## 👾 Features

|    |   Feature         | Description |
|----|-------------------|---------------------------------------------------------------|
| ⚙️  | **Architecture**  | The project follows a client-server architecture with separate components for stream handling, request handling, and transcription. |
| 🔩 | **Code Quality**  | The codebase is well-structured and clear. It includes good use of comments and proper naming conventions. |
| 📄 | **Documentation** | There is minimal documentation. More could be added for clarity on project setup and function usage. |
| 🔌 | **Integrations**  | This project integrates heavily with OpenAI for chatbots and sounddevice/soundfile for audio handling. |
| 🧩 | **Modularity**    | The project is modular with separate scripts for different functionalities. Relatively easy to extend and modify. |
| 🧪 | **Testing**       | There doesn't seem to be a dedicated testing suite. Unit and integration tests would be beneficial. |
| ⚡️  | **Performance**   | Uses streaming & concurrent operations to handle real-time audio, indicating good performance. |
| 🛡️ | **Security**      | Security measures are not clear from code inspection. More information is required. |
| 📦 | **Dependencies**  | Major dependencies include OpenAI, sounddevice, soundfile, numpy, requests and pydantic. |
| 🚀 | **Scalability**   | The project seems capable of handling increased load by virtue of its streaming architecture. |

---

## 📂 Repository Structure

```sh
└── dementia-assistant/
    ├── LICENSE
    ├── README.md
    ├── client
    │   ├── .env.demo
    │   ├── .gitignore
    │   ├── .vscode
    │   ├── api_helper.py
    │   ├── essential_data.py
    │   ├── function_calling
    │   ├── handler.py
    │   ├── main.py
    │   ├── main_assistant.py
    │   ├── openai_client.py
    │   ├── player.py
    │   ├── program_settings.py
    │   ├── requirements.txt
    │   ├── stream_constants.py
    │   ├── stream_handler.py
    │   ├── transcriber.py
    │   └── utils.py
    └── server
        ├── .env.demo
        ├── .gitignore
        ├── config.js
        ├── expressServer.js
        ├── index.js
        ├── lib
        ├── middleware
        ├── models
        ├── package-lock.json
        ├── package.json
        └── routes
```

---

## 🧩 Modules

<details closed><summary>client</summary>

| File | Summary |
| --- | --- |
| [main.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/main.py) | Main.py orchestrates the dementia-assistants client-side functionalities. It initializes and integrates the voice assistant, audio player, and transcription handler, and triggers the process of audio recording and transcribing. It also facilitates a verbose' mode for detailed logging. It is essentially the startup script for the assistant's operation. |
| [stream_handler.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/stream_handler.py) | This `stream_handler.py` file, found within the client' section of the dementia-assistant project, plays a significant role in managing and processing audio data. Specifically, it handles audio streaming which is essential for the real-time functionality required for the dementia-assistant's primary purpose of assisting those with dementia.The code leverages a few key libraries including `sounddevice` and `soundfile` for audio input and output operations, `numpy` for numerical computations, and `threading` for concurrent operations.It also interacts with the `transcriber.py` script to transcribe audio data, relying on the `transcriber_utils` library. Additionally, the file imports configurations from `program_settings` and `essential_data` to use in the audio stream handling process, specifically-`verbose`, `USER_GENDER`, and `USER_NAME`.In summary, `stream_handler.py` is critical to the projects aim of providing real-time dementia assistance, by managing audio data and preparing it for further processing and transcription. |
| [openai_client.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/openai_client.py) | OpenAI_client.py initializes and provides an instance of the OpenAI client in the dementia-assistant project. This component enables interaction with the OpenAI service, a fundamental aspect of the application's functionality to assist dementia patients. |
| [main_assistant.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/main_assistant.py) | Importing and using the OpenAI client for utilizing AI services.-Recording, transcribing, and managing speech-to-text tasks with the help of the `transcriber` module.-Utilizing essential user information like user gender and name for personalized interactions.-Leveraging the FunctionHandler from the `function_calling` directory to manage and handle function calls within the program.-Making use of the `api_helper` module to interact with server-side services.-Using multi-threading to handle multiple activities concurrently.The code in this file integrates these modules and functionalities to provide the main assistance features, such as personalized interactions, task handling, and providing support based on user needs. The `main_assistant.py` is a key part of the client-side application and plays a critical role in the overall architecture of the dementia-assistant system. |
| [essential_data.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/essential_data.py) | EssentialData.py in the client directory of the Dementia Assistant application assigns personal identifiers and crucial parameters, such as user and assistant names, gender, voice type, and important words, that guide the user-assistant interaction and conversation flow in the system. |
| [transcriber.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/transcriber.py) | The `transcriber.py` file is part of the `client` directory in the `dementia-assistant` repository. The role of this file is fundamental to the functioning of the Dementia Assistants conversational interface. This module is responsible for transcribing user and assistant interactions. With integration from `openai_client.py` and `essential_data.py`, it utilizes key data, including the assistant and user names, and important words, to structure a context-aware transcript.In addition, this module interacts with `program_settings.py` to take into account verbose settings that might regulate the level of detail in the transcriptions. The transcriptions created by this module offer critical insights into the dialogue flow and can be used for troubleshooting, user experience enhancements, and further development. |
| [program_settings.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/program_settings.py) | Program_settings.py enables the dementia assistant applications user settings configuration, facilitating the toggle of verbose mode on or off. It plays a central role in customizing user interactions within the broader application architecture. |
| [.env.demo](https://github.com/eloicito333/dementia-assistant/blob/main/client/.env.demo) | Hosts placeholder spaces for essential API keys. It initializes the environment variables for the OpenAI API key, the Internal API URL and the Internal API key, essential for the functioning of the dementia assistants client. |
| [api_helper.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/api_helper.py) | APIHelper in the api_helper.py module establishes a connection with the API and manages the interaction between the dementia-assistant client and the server. It posts and retrieves documents from SpokenDataDB, facilitating the conversion of spoken data into a transcribable format. |
| [stream_constants.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/stream_constants.py) | Stream_constants.py manages settings crucial to the audio recording and processing in the dementia-assistant client, encompassing specifications for speech detection, streaming frequency, block size, and parameters for audio transmission and buffering. |
| [utils.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/utils.py) | Utils.py in the client directory provides universal utility functions, specifically a flexible get_subscriptable function. This function fetches values from iterable data structures including dictionaries and handles exceptions, thereby reinforcing robustness and error management in the overall architecture of the dementia-assistant project. |
| [player.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/player.py) | This code file, `player.py`, belongs to the `client` directory of the `dementia-assistant` repository. In the overall architecture of the project, it plays a vital role in the audio processing functionality, especially focusing on audio playing operations. The primary purpose of this file is to create, manage, and control an audio player instance, utilizing a library for audio file processing and managing audio streams. Leveraging the open-source `openai_client`, this file establishes a client-server model to communicate with the OpenAI services. The `AudioPlayer` class shows the encapsulation of the coding logic related to the audio player, signifying the object-oriented programming approach used in the repository's framework. The settings and constants used in the player are imported from other modules in the repository, such as `program_settings` and `stream_constants`, indicating high modularity and the careful division of responsibilities within the codebase. As a part of its functionality, the `player.py` also incorporates threading for concurrent execution, which is crucial to achieving real-time interaction in the dementia-assistant application, improving its performance and user experience. |
| [requirements.txt](https://github.com/eloicito333/dementia-assistant/blob/main/client/requirements.txt) | Requirements.txt manages the necessary dependencies for the client-side of the dementia assistant application, specifying version-fixed packages to ensure consistent environment setup minimizing potential conflicts or issues. It underpins the functionality of other Python scripts in the client folder, such as transcription, streaming, and AI tasks. |
| [handler.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/handler.py) | Corrected_text` and an optional `confidential` dictionary. The `corrected_text` stores the refined and processed text, while the `confidential` dictionary can contain sensitive details that shouldnt be explicitly revealed. In the bigger picture of the repositorys architecture, this feature of structuring the program's output data aids in ensuring consistency and predictability of data returned by the program. It plays a fundamental role in data handling and management within the client part of the dementia-assistant project. |

</details>

<details closed><summary>client.function_calling</summary>

| File | Summary |
| --- | --- |
| [function_parent_class.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/function_calling/function_parent_class.py) | OpenAIFunction from function_parent_class.py provides a template for embedding AI functionalities in the dementia assistant project. It standardizes the interface for functions with a description, execution instructions, and a name while maintaining flexibility for varied use-cases. |
| [vector_data_retrieval.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/function_calling/vector_data_retrieval.py) | VectorDataRetrieval fetches information from historical conversations witnessed by the device, using context-specific parameters such as a text query, date range, or speakers name. It supports the dementia-assistant project by helping to find relevant past interactions, enhancing the systems contextual responsiveness. |
| [get_current_datetime.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/function_calling/get_current_datetime.py) | Obtaining the current date and time. Within the client-side functionality, it is especially tailored to interact with the OpenAI Function parent class, returning a formatted string containing the current weekday, date, and time upon invocation. |
| [function_handler.py](https://github.com/eloicito333/dementia-assistant/blob/main/client/function_calling/function_handler.py) | FunctionHandler within function_handler.py serves as a core coordinator, managing the execution of different functions like VectorDataRetrieval and GetCurrentDatetime in the dementia-assistants client-side architecture. It concurrently processes chat messages, applies necessary functions, and returns the results wrapped in response messages. |

</details>

<details closed><summary>server</summary>

| File | Summary |
| --- | --- |
| [config.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/config.js) | Serves as a centralized location for managing environment variables in the server-side component of the dementia-assistant project. Facilitates access to key configurations such as port settings, authentication data, API keys, and database connection details. |
| [expressServer.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/expressServer.js) | ExpressServer.js sets up the express server, establishes the API routing structure, incorporates authentication middleware, and integrates the spoken data routes. It also incorporates logging through the Morgan library. |
| [package.json](https://github.com/eloicito333/dementia-assistant/blob/main/server/package.json) | The package.json under the server directory primarily outlines the project metadata and dependency management for the Dementia Assistant's server-side operations. Additionally, it specifies various scripts including development, testing, and starting the server, facilitating the routine operations of this Express.js application. |
| [.env.demo](https://github.com/eloicito333/dementia-assistant/blob/main/server/.env.demo) | Server/.env.demo hosts essential environment variables necessary for the application's server side, facilitating functions such as database connectivity with MongoDB and interfacing with OpenAI via an API key, along with user authorisation. |
| [index.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/index.js) | Server/index.js orchestrates the initiation of the Dementia Assistant server. It creates an HTTP server using the application defined in expressServer.js and listens on the port specified in config.js. Key feedback on server initialization success and active port is provided through console logging. |
| [package-lock.json](https://github.com/eloicito333/dementia-assistant/blob/main/server/package-lock.json) | Dementia-assistant/client/api_helper.py================================================================================The `api_helper.py` file, located in the `client` directory of the dementia-assistant repository, serves as a helpful mediator for all API-related calls used by the system. It provides a high-level encapsulation of the API requests made by the client to various services, essentially acting as a bridge for communication between the client-side application and the server.The key functions of this file align well with the overarching goal of the repository, which is to develop an assistant for dementia patients. It contributes to this aim by ensuring smooth and efficient interactions with APIs, crucial for retrieving essential data and supporting functionalities. This could include gathering health-related information, handling feedback, or even managing user accounts.In essence, `api_helper.py` is a critical constituent of the client-side architecture contributing towards the seamless functionality of the dementia assistant. Please note that the specific API calls made by this file would depend on the needs and requirements of the dementia assistant application. |

</details>

<details closed><summary>server.middleware</summary>

| File | Summary |
| --- | --- |
| [auth.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/middleware/auth.js) | AuthMiddleware within auth.js facilitates an authentication check for incoming requests on the server side. It intercepts requests, compares the Authorization header value with the pre-set authentication string in the config file, and allows access or denies it, as appropriate, protecting sensitive routes in the dementia-assistant application. |

</details>

<details closed><summary>server.models</summary>

| File | Summary |
| --- | --- |
| [SpokenDataDoc.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/models/SpokenDataDoc.js) | SpokenDataDoc.js defines a database model for storing spoken data. It captures essential voice attributes such as the speakers identity, the text spoken, the date of the speech, and the embedding of the speech, essential for the dementia assistants operations. |

</details>

<details closed><summary>server.routes</summary>

| File | Summary |
| --- | --- |
| [spokenData.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/routes/spokenData.js) | This codebase is an architecture for a comprehensive Dementia Assistant' system. The system is split into the client and server sections with distinct roles. The server/routes/spokenData.js file, specifically, can be understood as the server-side routing system for managing spoken data. It holds a key role in the system's data transmission and management of voice-based interactions. Leveraging the Express.js Router, it facilitates RESTful API endpoints for client-server communication. It interacts with the OpenAI helper based in the lib directory to process natural language understanding and generation tasks. As well, the script connects to a database helper, also under lib, for persistent data storage and retrieval.Appreciating the wider repository, this file likely processes data from the client-side transcriptions (managed by transcriber.py'), and supports the server-side AI responses, ultimately aiding the provision of the assistant functionality for individuals living with dementia. |

</details>

<details closed><summary>server.lib</summary>

| File | Summary |
| --- | --- |
| [mongodb.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/lib/mongodb.js) | Establishes the connection to the MongoDB database using configuration parameters. It exports the database instance, enabling other parts of the application to interact with the database under a specified namespace. |
| [openai.js](https://github.com/eloicito333/dementia-assistant/blob/main/server/lib/openai.js) | Leverages OpenAI API to create a helper class within the server-side of the dementia assistant application. Its primary responsibility is to generate text embeddings, a crucial function for processing and understanding user input. |

</details>

---

## 🚀 Getting Started

### 🔖 Prerequisites

**Node.js**: `version 20.17.0`
**Python**: `version 3.12`

### 📦 Installation

Build the project from source:

1. Clone the dementia-assistant repository:
```sh
❯ git clone https://github.com/eloicito333/dementia-assistant/
```

2. Navigate to the project directory:
```sh
❯ cd dementia-assistant
```

3. Install the required dependencies on both client and server:

```sh
#server
❯ cd server
❯ npm i
```
```sh
#client
❯ cd client
❯ pip install -r requirements.txt
```


### 🤖 Usage
Before running this project, you need to **setup** the **environment variables** in `/server/.env` and `/client/.env` following the schemas in the `.env.demo` file of each directory.

To run the project, first boot the server:
```sh
#server
❯ npm start
```
Then initiate the client:

```sh
#client
❯ python main.py
```

---

## 📌 Project Roadmap

- [X] **`Task 1`**: <strike>Create basic voice assistant.</strike>
- [ ] **`Task 2`**: Create reminders functionality.
- [ ] **`Task 3`**: Buil the project in a Raspberry Pi Zero 2W.
- [ ] **`Task 4`**: Implement new fuctions for the LLM.

---

## 🤝 Contributing

Contributions are welcome! Here are several ways you can contribute:

- **[Report Issues](https://github.com/eloicito333/dementia-assistant/issues)**: Submit bugs found or log feature requests for the `dementia-assistant` project.
- **[Submit Pull Requests](https://github.com/eloicito333/dementia-assistant/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/eloicito333/dementia-assistant/discussions)**: Share your insights, provide feedback, or ask questions.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/eloicito333/dementia-assistant/
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/eloicito333/dementia-assistant/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=eloicito333/dementia-assistant">
   </a>
</p>
</details>

---

## 🎗 License

This project is protected under the [MODIFIED CREATIVE COMMONS](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.