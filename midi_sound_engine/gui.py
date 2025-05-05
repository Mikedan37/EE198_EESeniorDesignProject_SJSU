import tkinter as tk
from engine import play_note, stop_note

def key_press(note):
    play_note(note)

def key_release(note):
    stop_note(note)

# Build keys with tkinter or pygame as buttons