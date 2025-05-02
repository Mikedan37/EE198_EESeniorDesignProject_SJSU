#ifndef MIDI_DRIVER_H
#define MIDI_DRIVER_H

#include <stdint.h>

void send_midi_note_on(uint8_t note);
void send_midi_note_off(uint8_t note);

#endif