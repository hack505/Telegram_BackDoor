# Function Documentation

This document provides an overview of each function present in the Python script.

## cd(directory)
- **Description:** Change the current working directory.
- **Parameters:** `directory` - The directory to change to.
- **Usage:** `/cd <directory>`

## ls(directory)
- **Description:** List files in a directory.
- **Parameters:** `directory` - The directory to list files from.
- **Usage:** `/ls <directory>`

## system_info()
- **Description:** Retrieve system information such as hostname, IP address, processor, system type, and machine.
- **Usage:** Automatically triggered on bot startup.

## yo()
- **Description:** Greet the user with a simple message.
- **Usage:** `/yo`

## take_screenshot()
- **Description:** Capture a screenshot of the system.
- **Returns:** File name of the captured screenshot.

## start()
- **Description:** Start the bot and greet the user.
- **Usage:** `/start`

## help()
- **Description:** Display a list of available commands and their usage.
- **Usage:** `/help`

## content()
- **Description:** Provide information about the project and its owner.
- **Usage:** `/content`

## screenshot()
- **Description:** Take a screenshot of the system and send it to the user.
- **Usage:** `/screen`

## admin()
- **Description:** Provide information about the bot's administrator or owner.
- **Usage:** Internal function; not directly invoked by users.

## handle_text()
- **Description:** Handle incoming text messages and perform actions based on the content.
- **Usage:** Automatically invoked for all text messages received by the bot.

## run_command(command)
- **Description:** Execute a command on the system and send the result back to the user.
- **Parameters:** `command` - The command to execute.
- **Usage:** `/jarvis <command>`

## blocker(duration)
- **Description:** Block keyboard and mouse events for a specified duration (in minutes).
- **Parameters:** `duration` - The duration in minutes to block events.
- **Usage:** `/blocker <duration>`

## download_file(filename)
- **Description:** Download a file from the system and send it to the user.
- **Parameters:** `filename` - The name of the file to download.
- **Usage:** `/download <filename>`

## press_key(keys)
- **Description:** Simulate pressing keys on the system based on the user's command.
- **Parameters:** `keys` - The keys to press.
- **Usage:** `/press <keys>`

## arrow_key(direction)
- **Description:** Simulate pressing arrow keys on the system based on the user's command.
- **Parameters:** `direction` - The direction of the arrow key (up, down, left, right).
- **Usage:** `/arrow <direction>`

## download_requested_file(filename)
- **Description:** Respond to a user's request to download a specific file from the system and send it to the user.
- **Parameters:** `filename` - The name of the file to download.
- **Usage:** Internal function; not directly invoked by users.

## edit_message()
- **Description:** Edit a previously sent message with new content.
- **Usage:** Internal function; not directly invoked by users.
