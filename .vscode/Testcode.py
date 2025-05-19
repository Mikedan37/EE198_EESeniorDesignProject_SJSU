class NoteProcessor:
    def process(self, note):
        raise NotImplementedError

class NoteOnProcessor(NoteProcessor):
    def process(self, note):
        print(f"Note ON: {note}")

class NoteOffProcessor(NoteProcessor):
    def process(self, note):
        print(f"Note OFF: {note}")

# Usage
def process_note(note, processor):
    processor.process(note)

# Something New