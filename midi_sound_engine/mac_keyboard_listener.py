from pynput import keyboard
from engine import play_note, stop_note
import threading
import time

# Extended Mario Theme Notes (more than 2x longer)
MARIO_NOTES = [
    76, 76, 0, 76, 0, 72, 76, 0, 79, 0,         # E E - E - C E - G -
    0, 67, 0, 0, 72, 0, 67, 0, 64, 0,           # - G - - C - G - E -
    69, 0, 71, 70, 68, 66, 68, 70, 71, 69,       # A - B Bb A G A Bb B A
    67, 69, 71, 72, 74, 76, 77, 79,             # G A B C D E F G
    76, 74, 72, 71, 72                          # E D C B C
]

note_duration = 0.2
current_index = 0
lock = threading.Lock()

def play_mario_note(index):
    note = MARIO_NOTES[index]
    if note == 0:
        return  # rest
    play_note(note)
    time.sleep(note_duration)
    stop_note(note)

def on_press(key):
    global current_index
    try:
        char = key.char.lower()
        if char.isalpha():  # Only react to A–Z
            with lock:
                threading.Thread(target=play_mario_note, args=(current_index,)).start()
                current_index = (current_index + 1) % len(MARIO_NOTES)
    except AttributeError:
        pass

def start_keyboard_listener():
    print("⌨️ Type any letters (A–Z) to advance through the Mario melody...")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()