# keyboard and mouse blocker

credit - https://stackoverflow.com/questions/7529991/disable-or-lock-mouse-and-keyboard-in-python

*for windows*

```python
import time
from ctypes import windll
import pyHook
from threading import Timer
import win32gui
import logging


class blockInput():
    def OnKeyboardEvent(self, event):
        return False

    def OnMouseEvent(self, event):
        return False

    def unblock(self):
        logging.info(" -- Unblock!")
        if self.t.is_alive():
            self.t.cancel()
        try:
            self.hm.UnhookKeyboard()
        except:
            pass
        try:
            self.hm.UnhookMouse()
        except:
            pass

    def block(self, timeout=10, keyboard=True, mouse=True):
        self.t = Timer(timeout, self.unblock)
        self.t.start()

        logging.info(" -- Block!")
        if mouse:
            self.hm.MouseAll = self.OnMouseEvent
            self.hm.HookMouse()
        if keyboard:
            self.hm.KeyAll = self.OnKeyboardEvent
            self.hm.HookKeyboard()
        win32gui.PumpWaitingMessages()

    def __init__(self):
        self.hm = pyHook.HookManager()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    block = blockInput()
    block.block()

    import time
    t0 = time.time()
    while time.time() - t0 < 10:
        time.sleep(1)
        print(time.time() - t0)

    block.unblock()
    logging.info("Done.")

# https://stackoverflow.com/questions/7529991/disable-or-lock-mouse-and-keyboard-in-python

# anthor


def enable_input_block():
    windll.user32.BlockInput(True)
    print("Input block enabled")


def disable_input_block():
    windll.user32.BlockInput(False)
    print("Input block disabled")


# Enable input block
enable_input_block()

# Do something with input blocked (e.g., wait for 5 seconds)
time.sleep(5)

# Disable input block
disable_input_block()

```

*Cross-platform*

```python
import pynput
import time


def blocker(timeing):
    try:
        # Disable mouse and keyboard events
        mouse_listener = pynput.mouse.Listener(suppress=True)
        mouse_listener.start()
        keyboard_listener = pynput.keyboard.Listener(suppress=True)
        keyboard_listener.start()

        # sleep time for user to block
        time.sleep(timeing * 60)

        # Enable mouse and keyboard events
        mouse_listener.stop()
        keyboard_listener.stop()
    except Exception as e:
        print(e)


a = float(input("time in mintues to block: "))
blocker(a)

```