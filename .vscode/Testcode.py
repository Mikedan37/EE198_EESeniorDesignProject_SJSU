import time

class Debouncer:
    def __init__(self, wait):
        self.wait = wait
        self.time_of_last_call = 0

    def should_proceed(self):
        current_time = time.time()
        if current_time - self.time_of_last_call > self.wait:
            self.time_of_last_call = current_time
            return True
        return False

debouncer = Debouncer(0.3)

def handle_key_press(key_event):
    if debouncer.should_proceed():
        if key_event.pressed:
            process_note_on(key_event.note)
        else:
            process_note_off(key_event.note)

def process_note_on(note):
     print(f"Note ON: {note}")

def process_note_off(note):
     print(f"Note OFF: {note}")