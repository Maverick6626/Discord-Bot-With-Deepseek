# Discord Bot with Compliments, Insults, and Langchain Integration

This is a Python-based Discord bot that responds with compliments, insults, or engages in friendly conversation based on user input. It uses `discord.py` for Discord interaction and integrates `Langchain` and `Ollama` for generating dynamic and interactive responses.

## Features
- Responds to commands with a `+` prefix such as `+chat`, `+compliment`, and `+insult`.
- Uses Langchain for dynamic chatbot responses with memory.
- Compliment and insult responses are randomly selected from predefined lists.

## Requirements

Before running the bot, you need to install the necessary Python libraries.

### Step 1: Clone the repository

```
git clone https://github.com/Maverick6626/Discord-Bot-With-Deepseek.git
cd Discord-Bot-With-Deepseek
```
### Step 2: Add your Discord bot token in the .env file:

```
DISCORD_TOKEN=your_discord_token_here
```
### Step 3: Set up a virtual environment and install dependencies

```
python -m venv venv
.\venv\Scripts\activate
```
After activating your virtual environment, install the required dependencies by running:

```
pip install -r requirements.txt
```
### Step 4: Run the bot
Once you've cloned the repository, set up your .env file with the bot token, and installed the required dependencies, you can run the bot with:

```
python main.py
```
