# test_play.py (Polyphonic QWERTY + MIDI synth)
import keyboard
import threading
import time
from midi_utils import key_to_midi
from engine import play_note, shutdown
from pico_listener import midi_listener

POLL_INTERVAL = 0.01  # 10 ms
HOLD_REFRESH = 0.05   # 50 ms between repeated play_note

last_sent = {}  # note: last play time

def poll_keys():
    try:
        while True:
            now = time.time()
            for key in 'awsedftgyhujk':
                if keyboard.is_pressed(key):
                    midi_note = key_to_midi(key)
                    if midi_note and (
                        midi_note not in last_sent or
                        now - last_sent[midi_note] > HOLD_REFRESH
                    ):
                        play_note(midi_note)
                        last_sent[midi_note] = now
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        pass

def start_keyboard_polling():
    print("🔌 Starting Pico MIDI listener thread...")
    threading.Thread(target=midi_listener, daemon=True).start()
    
    print("🎹 Polyphonic Synth Active! Hold multiple keys (a–k). ESC to quit.")
    threading.Thread(target=poll_keys, daemon=True).start()

# ❌ DO NOT block main thread here if importing from monitor_and_launch.py
if __name__ == "__main__":
    start_keyboard_polling()
    keyboard.wait('esc')
    shutdown()
    print("🎵 Synth shut down.")