# Telegram Auto Responder

A Telegram auto-responder bot that sends a predefined message to users who write for the first time. It remembers users who have already received the message and ignores their subsequent messages.

## Features
- Sends a predefined message to new users.
- Remembers users who have already received the message.
- Stores user IDs in a JSON file for persistence between restarts.
- Easy to configure and deploy.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/telegram-auto-responder.git
   cd telegram-auto-responder
   
2. Clone the repository:
    ```bash
    pip install -r requirements.txt
   
3. Create a .env file and add your Telegram API credentials:
    ```bash
    API_ID=your_api_id
    API_HASH=your_api_hash
   
4. Run the bot:
    ```bash
    python main.py

## How it works
- When a user sends a message to your Telegram bot, it checks if the user has already received the predefined message.
- If it's the user's first message, the bot sends the predefined response and adds the user ID to a list stored in `responded_users.json`.
- If the user has already received a response, the bot ignores subsequent messages from that user.