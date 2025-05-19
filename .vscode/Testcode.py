import time

class KeyPressHandler:
    def __init__(self):
        self.last_key_press_time = {}
        self.debounce_time = 0.05  # debounce time in seconds

    def handle_key_press(self, key_event):
        current_time = time.time()
        last_press_time = self.last_key_press_time.get(key_event.note, 0)
        
        # If key press event happened within debounce time, ignore it
        if current_time - last_press_time < self.debounce_time:
            return
        
        self.last_key_press_time[key_event.note] = current_time

        if key_event.pressed:
            self.process_note_on(key_event.note)
        else:
            self.process_note_off(key_event.note)

    def process_note_on(self, note):
        print(f"Note ON: {note}")

    def process_note_off(self, note):
        print(f"Note OFF: {note}")

# Something New