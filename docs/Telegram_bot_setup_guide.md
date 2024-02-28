# Telegram Bot Setup Guide

This guide will walk you through the process of setting up a Telegram bot 

for guide in git go to [gif](gif/)

## Prerequisites

Before you begin, ensure you have the following:

- A Telegram account
- An internet connection

## Steps

### 1. Create a Telegram Bot

1. Open the Telegram app.
2. Search for the "BotFather" bot.
3. Start a chat with BotFather by clicking on "Start".
4. Use the `/newbot` command to create a new bot.
5. Follow the prompts to provide a name and username for your bot.
6. Once the bot is created, BotFather will provide you with a token. **Save this token**, as you'll need it later.
   
### 2. Obtain your chat id

1. Open the Telegram app.
2. Search for the User Info Bot by typing "@UserInfoBot" in the search bar.
3. Start a chat with the User Info Bot by clicking on its name in the search results.
4. Once the chat is opened, you can send any message to the bot.
5. The User Info Bot will reply with information about your account, including your chat ID.
   
### 3. Configuration
Create a `config.json` file with your Telegram bot token and chat ID. Example:
```json
{
    "token": "YOUR_TELEGRAM_BOT_TOKEN",
    "chat_id": "YOUR_CHAT_ID"
}
```

### 4. set up command list 

1. Go to BotFather
2. type `/setcommands`
3. select you bot 
4. now, Paste this following below text

```bash
start - Begin interaction
help - Get assistance
content - View project info
screen - Take a screenshot
jarvis - Execute a command
yo - Greet the user
press - Press keys
arrow - Use arrow keys
download - Download a file
cd - Change directory
ls - List files
blocker - Block input
```
*note:* via this you can see those commands on you bot command list which can make you life easier

### I hope you successful completed all steps!
