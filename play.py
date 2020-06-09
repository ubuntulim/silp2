import os
import subprocess
import glob
from pynput import keyboard

soundlist = {}

for file in glob.glob('drum_sound/*.wav'):
    _, filename = file.split('/')
    key, _ = filename.split('.')
    soundlist.update({key: file})

sound = list(soundlist.keys())
play = 'play'

FNULL = open(os.devnull, 'w')

def on_press(key):
    try:
        if key == keyboard.Key.esc:
            return False
        i = int(key.char)
        if 0 <= i and i <= len(sound)-1:
            print_name = sound[i]
            subprocess.Popen([play, soundlist[sound[i]]], stdout=FNULL, stderr = subprocess.STDOUT)
        else:
            print_name = 'None'

        print(f"\t--> sound[{i+1}]: {print_name:20}", end='\r', flush=True)
    except AttributeError:
        print(f"\t--> special key: {key} pressed", end='\r', flush=True)
    except:
        print(f'\t--> {type(key.char)}  {"":10}', end='\r', flush=True)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
