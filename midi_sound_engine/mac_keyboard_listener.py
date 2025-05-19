from pynput import keyboard
from engine import play_note, stop_note
from collections import deque
from concurrent.futures import ThreadPoolExecutor
import threading
import time

# Extended Mario Theme Notes (more than 2x longer)
MARIO_NOTES = deque([
    76, 76, 0, 76, 0, 72, 76, 0, 79, 0,         # E E - E - C E - G -
    0, 67, 0, 0, 72, 0, 67, 0, 64, 0,           # - G - - C - G - E -
    69, 0, 71, 70, 68, 66, 68, 70, 71, 69,       # A - B Bb A G A Bb B A
    67, 69, 71, 72, 74, 76, 77, 79,             # G A B C D E F G
    76, 74, 72, 71, 72                          # E D C B C
])

note_duration = 0.2
lock = threading.Lock()
executor = ThreadPoolExecutor(max_workers=10)

def play_mario_note():
    note = MARIO_NOTES[0]
    if note == 0:
        return  # rest
    play_note(note)
    time.sleep(note_duration)
    stop_note(note)

def on_press(key):
    try:
        if key.char.isalpha():  # Only react to A–Z
            with lock:
                executor.submit(play_mario_note)
                MARIO_NOTES.rotate(-1)
    except AttributeError:
        pass

def start_keyboard_listener():
    print("⌨️ Type any letters (A–Z) to advance through the Mario melody...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()