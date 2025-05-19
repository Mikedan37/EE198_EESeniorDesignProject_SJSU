class NoteObserver:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def notify(self, note):
        for observer in self._observers:
            observer.update(note)

class NoteOnObserver(NoteObserver):
    def update(self, note):
        print(f"Note ON: {note}")

class NoteOffObserver(NoteObserver):
    def update(self, note):
        print(f"Note OFF: {note}")

note_on_observer = NoteOnObserver()
note_off_observer = NoteOffObserver()

def process_note_on(note):
    note_on_observer.notify(note)

def process_note_off(note):
    note_off_observer.notify(note)