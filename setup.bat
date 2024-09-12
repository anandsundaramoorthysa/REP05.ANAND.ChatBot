@echo off
setlocal

:: Check Python version
for /f "tokens=2 delims= " %%v in ('python --version') do (
    set PYTHON_VERSION=%%v
)

echo Detected Python version: %PYTHON_VERSION%

:: Set required version
set REQUIRED_VERSION=3.9.13

:: Extract major, minor, and patch versions
for /f "tokens=1,2,3 delims=." %%a in ("%PYTHON_VERSION%") do (
    set MAJOR_VERSION=%%a
    set MINOR_VERSION=%%b
    set PATCH_VERSION=%%c
)

:: Compare versions
if "%MAJOR_VERSION%.%MINOR_VERSION%.%PATCH_VERSION%"=="%REQUIRED_VERSION%" (
    echo Python version is correct.
) else (
    echo Error: Python %REQUIRED_VERSION% is required. Please install the correct version.
    exit /b 1
)

:: Create virtual environment
echo Creating virtual environment 'envir'...
python -m venv envir

:: Activate virtual environment
call envir\Scripts\activate

:: Install dependencies
echo Installing dependencies...
python -m pip install --upgrade pip

:: Install all the required packages
python -m pip install blinker==1.8.2 certifi==2024.8.30 charset-normalizer==3.3.2 click==8.1.7 colorama==0.4.6 ^
    diffusers==0.30.2 filelock==3.16.0 Flask==3.0.3 fsspec==2024.9.0 huggingface-hub==0.24.6 idna==3.8 ^
    importlib_metadata==8.5.0 itsdangerous==2.2.0 Jinja2==3.1.4 MarkupSafe==2.1.5 mpmath==1.3.0 networkx==3.2.1 ^
    numpy==2.0.2 packaging==24.1 pillow==10.4.0 pip==24.2 psutil==6.0.0 PyYAML==6.0.2 regex==2024.7.24 requests==2.32.3 ^
    safetensors==0.4.5 setuptools==58.1.0 sympy==1.13.2 tokenizers==0.19.1 torch==2.4.1 tqdm==4.66.5 transformers==4.44.2 ^
    typing_extensions==4.12.2 urllib3==2.2.2 Werkzeug==3.0.4 zipp==3.20.1

:: Run the app
echo Running the app...
python app.py

endlocal
pause
