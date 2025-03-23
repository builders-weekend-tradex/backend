# TradEx Backend

## Prerequisites
Ensure you have the following installed:

- [Python 3](https://www.python.org/downloads/)
- [Make](https://www.gnu.org/software/make/)

## Installation
### 1. Clone the repository
```
git clone <repository_url>
cd <repository_folder>
```
### 2. Set Up Environment Variables
This project requires an `.env` file to store API keys. Create a `.env` file in the root directory and add the following:
```
# NewsAPI
API_KEY=your_newsapi_key

# Xpress AI (Lexi)
LEXI_URL=your_lexi_chatbot_url
LEXI_API_KEY=your_lexi_chatbot_api_key
```
Replace `your_newsapi_key`, `your_lexi_chatbot_url` and `your_lexi_chatbot_api_key` with the actual credentials.
> **Note:** The AI chatbot used in this project is **Xpress AI's chatbot Lexi**. However, you can use a different chatbot by changing the references of `LEXI_URL` and `LEXI_API_KEY` in the code.

### 3. Install dependencies
Use `make` to set up a virtual environment and install dependencies:
```
make install
```
This will:
- Create a Python virtual environment (`venv`)
- Install dependencies from `requirements.txt`
<br>
    
> **Note:** If you are on Windows, the virtual environment activation script will be in `venv/Scripts/activate`, while on macOS/Linux it will be in `venv/bin/activate`.

## Running the Server
To start the FastAPI server, use:
```
make runserver
```
This runs the server using `fastapi dev main.py`
<br>

## Managing Dependencies
### Freeze Installed Packages
To update `requirements.txt` with installed packages:
```
make freeze
```

### Clean Up
To remove the virtual environment and any generated files:
```
make clean
```
