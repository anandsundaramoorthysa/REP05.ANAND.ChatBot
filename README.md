# AI Chatbot Setup

This project contains an AI-powered chatbot that leverages Hugging Face's GPT-2 models for text generation. It features a simple Flask web interface to interact with the chatbot. This guide will walk you through setting up the environment, installing dependencies, and running the chatbot. 

**Note:**: You must clone/install and use folder in name "chatbot"

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Running the Application](#running-the-application)
- [Known Issues](#known-issues)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

This chatbot utilizes pre-trained GPT-2 models to generate responses based on user input. The chatbot allows you to switch between different GPT-2 model sizes dynamically and provides a web-based interface to communicate with the AI.

## Features

- **Pre-trained GPT-2 Models**: Supports text generation using GPT-2 models.
- **Dynamic Model Switching**: Change between different GPT-2 models via the web interface.
- **Simple Web Interface**: Users can interact with the chatbot through a web form.
- **Predefined Responses**: The chatbot includes predefined responses for common queries.
- **Easy Setup**: Quick to deploy with all necessary steps automated in a batch script.

## Technologies Used

- **Python 3.9.13**
- **Flask**: Web framework.
- **Hugging Face Transformers**: GPT-2 models.
- **HTML/CSS/JavaScript**: Front-end for the chatbot interface.

## Setup

### Prerequisites

Before you begin, ensure you have:

- **Python 3.9.13** installed on your system. [Download here](https://www.python.org/downloads/release/python-3913/).
- **Git** (optional, to clone the repository).

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/a1n13a1n13d4/REP05.ANAND.ChatBot/
   cd REP05.ANAND.ChatBot
   ```

2. **Run the `setup.bat` Script**:

   The `setup.bat` file automates the setup process, which includes checking your Python version, creating a virtual environment, installing dependencies, and running the app.

   - **Double-click** `setup.bat` or run it from the command line:
   
     ```bash
     .\setup.bat
     ```

#### What the script does:
- **Python Version Check**: The script checks if Python 3.9.13 is installed. If the version is incorrect, it will stop and ask you to install the required version.
- **Virtual Environment Setup**: If the Python version is correct, the script creates a virtual environment named `envir`.
- **Dependency Installation**: Installs the necessary Python packages into the virtual environment.
- **Running the App**: Finally, the script runs the `app.py` file to start the chatbot.

## Running the Application

After successfully running the `setup.bat` script, the chatbot will be available on `localhost`. You can open the URL in your web browser and interact with the chatbot.

To manually run the app after setup:
1. Activate the virtual environment:
   ```bash
   .\envir\Scripts\activate
   ```

2. Run the Flask app:
   ```bash
   python app.py
   ```

## Known Issues

- **Python Version Errors**: If you get an error about the Python version, make sure you have exactly Python 3.9.13 installed.
- **Model Loading Delays**: GPT-2 models may take time to download the first time they are used. Be patient while the models are cached.
- **Path Issue:**: When they coding not worked even after run the setup.bat file. In the app.py the had line
```bash
model_dir = os.getenv('MODEL_DIR', '/models/')
```
- Replace the path with your system had models folder path.
- **Folder Name:**: The Folder Name must in "chatbot".

## Contributing

We welcome contributions from the community! To contribute, please follow these steps:

1. **Fork the Repository**: Create a copy of this repository under your own GitHub account.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/a1n13a1n13d4/REP05.ANAND.ChatBot.git
   cd REP05.ANAND.ChatBot
   ```

3. **Create a New Branch**: Create a branch for your changes.
   ```bash
   git checkout -b your-feature-branch
   ```

4. **Make Your Changes**: Edit the files and commit your changes.
   ```bash
   git add .
   git commit -m "Describe your changes"
   ```

5. **Push Your Changes**: Push the changes to your forked repository.
   ```bash
   git push origin your-feature-branch
   ```

6. **Submit a Pull Request**: Go to the original repository and submit a pull request for review.

For any inquiries or if you need further assistance, please contact me at:

- **Email**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Enquiry%20about%20Chat%20Bot%20Project&body=Dear%20Gagan,%0A%0A%20I%20have%20an%20enquiry%20about%20the%20Chat%20Bot%20Project.%20Please%20provide%20the%20necessary%20details.%0A%0A%20Thank%20you.%0A%0A%20Best%20regards,%0A%20[Your%20Name])

- **LinkedIn**: [Anand S](https://www.linkedin.com/in/anands37/)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/a1n13a1n13d4/REP05.ANAND.ChatBot/blob/main/LICENSE) file for details.
