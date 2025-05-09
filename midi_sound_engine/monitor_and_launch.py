# monitor_and_launch.py

from unified_listener import launch_listeners  # ✅ New: single call to launch all
from synth_menu import SynthMenuBarApp
from engine import shutdown, start_audio_engine

def main():
    try:
        print("🔊 Starting audio engine (main thread)...")
        start_audio_engine()  # ✅ Must be on main thread for sounddevice stability

        print("🔌 Launching background listeners...")
        launch_listeners()  # ✅ Serial, MIDI, QWERTY, etc.

        print("🚀 Launching menu bar...")
        SynthMenuBarApp().run()

    except KeyboardInterrupt:
        shutdown()
        print("🛑 Synth system shut down.")

if __name__ == "__main__":
    main()