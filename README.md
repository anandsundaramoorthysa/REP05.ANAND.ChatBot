# AI Chatbot Setup

This project contains an AI-powered chatbot that leverages Hugging Face's GPT-2 models for text generation. It features a simple Flask web interface to interact with the chatbot. This guide will walk you through setting up the environment, installing dependencies, and running the chatbot.

**Note**: You must clone/install and use the folder named "chatbot".

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
- [Contact Me](#contact-me)
- [Acknowledge](#acknowledge)

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
   git clone https://github.com/anandsundaramoorthysa/REP05.ANAND.ChatBot/
   cd REP05.ANAND.ChatBot
   ```

2. **Option 1: Run the `setup.bat` Script**

   The `setup.bat` file automates the setup process, including checking your Python version, creating a virtual environment, installing dependencies, and running the app.

   - **Double-click** `setup.bat` or run it from the command line:
   
     ```bash
     .\setup.bat
     ```

3. **Option 2: Install Dependencies Manually**

   If you prefer to install dependencies manually, run the following command:

   ```bash
   pip install blinker==1.8.2 certifi==2024.8.30 charset-normalizer==3.3.2 click==8.1.7 colorama==0.4.6 diffusers==0.30.2 filelock==3.16.0 Flask==3.0.3 fsspec==2024.9.0 huggingface-hub==0.24.6 idna==3.8 importlib_metadata==8.5.0 itsdangerous==2.2.0 Jinja2==3.1.4 MarkupSafe==2.1.5 mpmath==1.3.0 networkx==3.2.1 numpy==2.0.2 packaging==24.1 pillow==10.4.0 pip==24.2 psutil==6.0.0 PyYAML==6.0.2 regex==2024.7.24 requests==2.32.3 safetensors==0.4.5 setuptools==58.1.0 sympy==1.13.2 tokenizers==0.19.1 torch==2.4.1 tqdm==4.66.5 transformers==4.44.2 typing_extensions==4.12.2 urllib3==2.2.2 Werkzeug==3.0.4 zipp==3.20.1
   ```

4. **Option 3: Use a `requirements.txt` File**

   Alternatively, you can save the dependencies in a `requirements.txt` file and install them with:

   ```bash
   pip install -r requirements.txt
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
- **Path Issue**: If the code does not work even after running the `setup.bat` file, make sure to replace the path in `app.py`:
   ```bash
   model_dir = os.getenv('MODEL_DIR', '/models/')
   ```
   - Replace `/models/` with the correct path where your models are stored.
   - **Folder Name**: The folder name must be "chatbot".

## Contribution

We welcome contributions from the community! To contribute, please follow these steps:

1. **Fork the Repository**: Create a copy of this repository under your own GitHub account.

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/anandsundaramoorthysa/REP05.ANAND.ChatBot.git
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

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/anandsundaramoorthysa/REP05.ANAND.ChatBot/blob/main/LICENSE) file for details.

## Contact Me

If you have any questions or would like to collaborate, feel free to reach out:

- **Email**: [sanand03072005@gmail.com](mailto:sanand03072005@gmail.com?subject=Enquiry%20about%20Chat%20Bot%20Project&body=Dear%20Gagan,%0A%0A%20I%20have%20an%20enquiry%20about%20the%20Chat%20Bot%20Project.%20Please%20provide%20the%20necessary%20details.%0A%0A%20Thank%20you.%0A%0A%20Best%20regards,%0A%20[Your%20Name])

- **LinkedIn**: [Anand S](https://www.linkedin.com/in/anandsundaramoorthysa/)

## Acknowledge

We acknowledge the use of pre-trained models from Hugging Face and other open-source libraries that made this project possible.
