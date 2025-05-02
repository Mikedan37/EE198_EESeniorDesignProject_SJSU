// USB Handler Logic
#include <stdio.h>
#include "usb_handler.h"

bool get_mode() {
    static int state = 0;
    state = !state;
    printf("Mode: %s\n", state ? "MIDI" : "QWERTY");
    return state;
}

int get_simulated_key() {
    return get_mode() ? 60 : 'A';
}

void send_midi_note_on(int note, int velocity) {
    printf("[MIDI] Note ON: %d, Velocity: %d\n", note, velocity);
}

void send_hid_key(int keycode) {
    printf("[HID] Key Pressed: %c\n", keycode);
}