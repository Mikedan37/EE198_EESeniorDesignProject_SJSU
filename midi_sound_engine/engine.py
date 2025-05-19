# engine.py

import numpy as np
import sounddevice as sd
import threading
import time

SAMPLE_RATE = 44100
BLOCK_SIZE = 512
TIMEOUT = 0.3  # seconds to hold before auto stop
MIDI_CONSTANT = 69

class AudioEngine:
    def __init__(self):
        self.lock = threading.Lock()
        self.playing = threading.Event()
        self.held_notes = set()
        self.note_timestamps = {}
        self.phase_dict = {}
        self.last_note = None
        self.last_freq = None

    def freq_from_midi(self, note):
        return 440.0 * (2 ** ((note - MIDI_CONSTANT) / 12))

    def play_note(self, note, velocity=100):
        with self.lock:
            self.held_notes.add(note)
            self.note_timestamps[note] = time.time()
            if note not in self.phase_dict:
                self.phase_dict[note] = 0.0
            self.last_note = note
            self.last_freq = self.freq_from_midi(note)
            print(f"[ENGINE] ▶️ Playing {note} ({self.last_freq:.2f} Hz)")

    def stop_note(self, note):
        with self.lock:
            self._stop_note(note)

    def _stop_note(self, note):
        if note in self.held_notes:
            self.held_notes.remove(note)
            print(f"[ENGINE] ⏹️ Stopped {note}")

    # ... rest of the methods ...

engine = AudioEngine()