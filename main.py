import pynput.keyboard

def on_press(key):
    try:
        print("Key pressed: {0}".format(key.char))
    except AttributeError:
        print("Special key pressed: {0}".format(key))

def on_release(key):
    print("Key released: {0}".format(key))
    if key == pynput.keyboard.Key.esc:
        # Stop the program
        return False

with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()