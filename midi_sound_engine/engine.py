# engine.py

import numpy as np
import sounddevice as sd
import threading
import time

SAMPLE_RATE = 44100
BLOCK_SIZE = 512
TIMEOUT = 0.3  # seconds to hold before auto stop

# 🎛️ Engine state
lock = threading.Lock()
playing = True
held_notes = set()
note_timestamps = {}
phase_dict = {}

# 🎹 Display tracking
last_note = None
last_freq = None

def freq_from_midi(note):
    return 440.0 * (2 ** ((note - 69) / 12))

def play_note(note, velocity=100):
    global last_note, last_freq
    with lock:
        held_notes.add(note)
        note_timestamps[note] = time.time()
        if note not in phase_dict:
            phase_dict[note] = 0.0
        last_note = note
        last_freq = freq_from_midi(note)
        print(f"[ENGINE] ▶️ {note} ({last_freq:.2f} Hz)")

def stop_note(note):
    with lock:
        if note in held_notes:
            held_notes.remove(note)
            print(f"[ENGINE] ⏹️ Note {note} manually stopped")

def get_last_note_info():
    with lock:
        return last_note, last_freq

def audio_callback(outdata, frames, time_info, status):
    if status:
        print("⚠️ Audio callback:", status)

    buffer = np.zeros(frames, dtype=np.float32)
    now = time.time()

    with lock:
        for note in list(held_notes):
            if now - note_timestamps.get(note, 0) > TIMEOUT:
                held_notes.remove(note)
                print(f"[ENGINE] ⏹️ Auto stop: {note}")
                continue

            freq = freq_from_midi(note)
            phase = phase_dict.get(note, 0.0)
            t = np.arange(frames)
            wave = np.sin(2 * np.pi * freq * t / SAMPLE_RATE + phase)
            phase += 2 * np.pi * freq * frames / SAMPLE_RATE
            phase_dict[note] = phase % (2 * np.pi)
            buffer += wave

        if np.max(np.abs(buffer)) > 0:
            buffer /= np.max(np.abs(buffer))

    outdata[:] = buffer.reshape(-1, 1)

def audio_loop():
    print("🔊 Starting audio engine...")
    with sd.OutputStream(
        samplerate=SAMPLE_RATE,
        blocksize=BLOCK_SIZE,
        channels=1,
        dtype='float32',
        callback=audio_callback
    ):
        while playing:
            sd.sleep(100)

def shutdown():
    global playing
    playing = False
    print("🛑 Audio engine shutdown requested.")

# 🚀 Launch audio thread when this module is imported
threading.Thread(target=audio_loop, daemon=True).start()
print("🎧 Synth engine running (timeout-based key hold logic)")