import time
import threading
from pico_listener import midi_listener
from test_play import start_keyboard_polling
from synth_menu import SynthMenuBarApp
from engine import shutdown

def launch_background_components():
    print("🔌 Starting background threads...")
    threading.Thread(target=midi_listener, daemon=True).start()
    start_keyboard_polling()

def main():
    try:
        print("🔊 Starting audio engine...")
        launch_background_components()

        print("🎧 Synth engine running (timeout-based key hold logic)")
        print("🚀 Launching menu bar...")

        # ✅ Menu bar must run on the main thread
        SynthMenuBarApp().run()
    except KeyboardInterrupt:
        shutdown()
        print("🛑 Synth system shut down.")

if __name__ == "__main__":
    main()