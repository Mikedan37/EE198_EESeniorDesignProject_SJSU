#include <USB-MIDI.h>

USBMIDI_CREATE_DEFAULT_INSTANCE();

void setup() {
  // nothing needed for MIDI
}

void loop() {
  MIDI.sendNoteOn(60, 127, 1); // C4 note on
  delay(500);
  MIDI.sendNoteOff(60, 0, 1);  // C4 note off
  delay(500);
}