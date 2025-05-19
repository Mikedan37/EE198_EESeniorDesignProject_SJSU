# monitor_and_launch.py

from unified_listener import launch_listeners
from synth_menu import SynthMenuBarApp
from engine import shutdown, start_audio_engine
import logging

def main():
    try:
        logging.info("Starting audio engine (main thread)...")
        start_audio_engine()

        logging.info("Launching background listeners...")
        launch_listeners()

        logging.info("Launching menu bar...")
        SynthMenuBarApp().run()

    except KeyboardInterrupt:
        shutdown()
        logging.info("Synth system shut down.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        shutdown()

if __name__ == "__main__":
    logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    main()