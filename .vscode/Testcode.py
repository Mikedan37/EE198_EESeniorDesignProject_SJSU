# TODO: Add input debounce logic
def handle_key_press(key_event):
    # It's a good practice to validate the input before processing it.
    # Here, we should check if key_event and key_event.note are not None.
    if key_event and key_event.note and key_event.pressed:
        process_note_on(key_event.note)
    elif key_event and key_event.note:
        process_note_off(key_event.note)
    else:
        print("Invalid key event")

def process_note_on(note):
    # Using string formatting can potentially lead to security issues.
    # It's better to use parameterized print statements.
    print("Note ON: %s", note)

def process_note_off(note):
    # Using string formatting can potentially lead to security issues.
    # It's better to use parameterized print statements.
    print("Note OFF: %s", note)

# Something New  No changes
# TODO: Fix this function
def broken_code():
    print("oops")....