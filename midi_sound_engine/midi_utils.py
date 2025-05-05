# midi_utils.py
# Map QWERTY keys to MIDI note numbers (C4 to C5)

qwerty_to_midi = {
    'a': 60,  # C4
    'w': 61,
    's': 62,
    'e': 63,
    'd': 64,
    'f': 65,
    't': 66,
    'g': 67,
    'y': 68,
    'h': 69,
    'u': 70,
    'j': 71,
    'k': 72   # C5
}

def key_to_midi(key_char):
    return qwerty_to_midi.get(key_char.lower())