import random

# Very simple next-tone Markov model
note_transitions = {
    60: [62, 64, 67],
    62: [64, 65],
    64: [65, 67, 69],
    # ...
}

def predict_next(note):
    return random.choice(note_transitions.get(note, [note]))