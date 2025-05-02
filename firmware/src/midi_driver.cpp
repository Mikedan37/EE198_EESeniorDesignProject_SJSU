#include <stdint.h>
#include "midi_driver.h"

void send_midi_note_on(uint8_t note) {
  uint8_t msg[3] = {0x90, note, 100}; // Note On, channel 1, velocity 100
  usb_midi.write(msg, 3);
}

void send_midi_note_off(uint8_t note) {
  uint8_t msg[3] = {0x80, note, 0}; // Note Off, channel 1
  usb_midi.write(msg, 3);
}