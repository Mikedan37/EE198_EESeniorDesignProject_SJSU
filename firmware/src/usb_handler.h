#ifndef USB_HANDLER_H
#define USB_HANDLER_H

#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

void send_midi_note_on(int note, int velocity);
void send_hid_key(int keycode);
bool get_mode();
int get_simulated_key();

#ifdef __cplusplus
}
#endif

#endif