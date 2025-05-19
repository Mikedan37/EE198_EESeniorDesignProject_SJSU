class NoteObserver:
    def __init__(self):
        self._observers = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def notify(self, note):
        for observer in self._observers:
            observer(note)

note_observer = NoteObserver()

def process_note_on(note):
    note_observer.notify(note)

def process_note_off(note):
    print(f"Note OFF: {note}")