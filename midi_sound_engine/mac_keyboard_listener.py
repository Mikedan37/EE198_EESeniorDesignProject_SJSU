import keyboard
from engine import play_note, stop_note

# QWERTY → MIDI note map
KEY_TO_NOTE = {
    'a': 60,  # C4
    's': 62,  # D4
    'd': 64,  # E4
    'f': 65,  # F4
    'g': 67,  # G4
   
}

active_notes = set()

def on_key_down(e):
    key = e.name.lower()
    if key in KEY_TO_NOTE and key not in active_notes:
        note = KEY_TO_NOTE[key]
        play_note(note)
        active_notes.add(key)

def on_key_up(e):
    key = e.name.lower()
    if key in KEY_TO_NOTE and key in active_notes:
        note = KEY_TO_NOTE[key]
        stop_note(note)
        active_notes.remove(key)

def start_keyboard_listener():
    print("⌨️ Listening to Mac keyboard input...")
    keyboard.on_press(on_key_down)
    keyboard.on_release(on_key_up)
    keyboard.wait()  # Keep the script alive