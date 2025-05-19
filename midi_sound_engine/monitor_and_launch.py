from unified_listener import launch_listeners
from synth_menu import SynthMenuBarApp
from engine import shutdown, start_audio_engine
import threading

def main():
    try:
        print("🔊 Starting audio engine (main thread)...")
        audio_engine_thread = threading.Thread(target=start_audio_engine)
        audio_engine_thread.start()

        print("🔌 Launching background listeners...")
        listener_thread = threading.Thread(target=launch_listeners)
        listener_thread.start()

        print("🚀 Launching menu bar...")
        app = SynthMenuBarApp()
        app.run()

        # Wait for the threads to complete
        audio_engine_thread.join()
        listener_thread.join()

    except KeyboardInterrupt:
        print("🛑 Synth system shut down.")
        shutdown_thread = threading.Thread(target=shutdown)
        shutdown_thread.start()
        shutdown_thread.join()

if __name__ == "__main__":
    main()