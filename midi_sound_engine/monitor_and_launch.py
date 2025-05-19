# monitor_and_launch.py

import logging
from unified_listener import launch_listeners  
from synth_menu import SynthMenuBarApp
from engine import shutdown, start_audio_engine

# Configure logging
logging.basicConfig(level=logging.INFO)

def main():
    """
    Main function to start the audio engine, launch listeners and menu bar.
    """
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
        logging.error("An unexpected error occurred: ", exc_info=True)

if __name__ == "__main__":
    main()