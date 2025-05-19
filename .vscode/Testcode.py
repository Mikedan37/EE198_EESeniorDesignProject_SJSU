import time

# Define a debounce delay (in seconds)
DEBOUNCE_DELAY = 0.05

# Store the time of the last key press event
last_key_press_time = None

def handle_key_press(key_event):
    global last_key_press_time

    # Get the current time
    current_time = time.time()

    # If this is the first key press event or if the delay since the last key press event is more than the debounce delay
    if last_key_press_time is None or current_time - last_key_press_time > DEBOUNCE_DELAY:
        # Update the time of the last key press event
        last_key_press_time = current_time

        # Validate the key event
        if key_event.validate():
            if key_event.pressed:
                process_note_on(key_event.note)
            else:
                process_note_on(key_event.note)

def process_note_on(note):
    print(f"Note ON: {note}")

def process_note_off(note):
    print(f"Note OFF: {note}")