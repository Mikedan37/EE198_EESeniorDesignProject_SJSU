class NoteProcessor:
    def __init__(self):
        self.note_on = False

    def handle_key_press(self, key_event):
        if key_event.pressed:
            if not self.note_on:
                self.note_on = True
                self.process_note_on(key_event.note)
        else:
            if self.note_on:
                self.note_on = False
                self.process_note_off(key_event.note)

    def process_note_on(self, note):
        print(f"Note ON: {note}")

    def process_note_off(self, note):
        print(f"Note OFF: {note}")