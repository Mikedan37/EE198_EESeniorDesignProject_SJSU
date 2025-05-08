import threading
from pico_listener import midi_listener
from mac_keyboard_listener import start_keyboard_listener
import engine  # This ensures the engine starts up

# Run MIDI and keyboard listeners on separate threads
t1 = threading.Thread(target=midi_listener, daemon=True)
t2 = threading.Thread(target=start_keyboard_listener, daemon=True)

t1.start()
t2.start()

# Keep main thread alive
try:
    while True:
        pass
except KeyboardInterrupt:
    print("👋 Exiting gracefully...")
    engine.shutdown()