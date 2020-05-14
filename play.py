import subprocess
import glob
from pynput import keyboard


soundlist = []

for file in glob.glob('drum_sound/*.wav'):
   soundlist.extend({file})

def on_press(key):
    try:
        i = int(key.char)
        if 0 <= i and i <= len(soundlist)-1 :      
            subprocess.Popen(['play', soundlist[i]], stdout=subprocess.PIPE, stderr = subprocess.PIPE)
    except AttributeError:
        print('unexpected key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(key))
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
