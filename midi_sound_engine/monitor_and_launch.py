# monitor_and_launch.py

# Importing necessary modules
from unified_listener import launch_listeners  # Single call to launch all listeners
from synth_menu import SynthMenuBarApp
from engine import shutdown, start_audio_engine

def main():
    """Main function to start audio engine, launch listeners and menu bar."""
    try:
        # Starting audio engine
        print("🔊 Starting audio engine (main thread)...")
        start_audio_engine()  # Must be on main thread for sounddevice stability

        # Launching background listeners
        print("🔌 Launching background listeners...")
        launch_listeners()  # Serial, MIDI, QWERTY, etc.

        # Launching menu bar
        print("🚀 Launching menu bar...")
        SynthMenuBarApp().run()  # Running the SynthMenuBarApp

    except KeyboardInterrupt:
        # Handling keyboard interrupt and shutting down
        shutdown()
        print("🛑 Synth system shut down.")

if __name__ == "__main__":
    main()  # Calling the main function