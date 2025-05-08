// #include "pico/stdlib.h"
// #include "bsp/board.h"
// #include "tusb.h"
// #include "gpio_driver.h"

// // Notes: C4, D4, E4, F4, G4
// const uint8_t midi_notes[NUM_KEYS] = {60, 62, 64, 65, 67};
// // HID keycodes: A, B, C, D, E
// const uint8_t hid_keycodes[NUM_KEYS] = {0x04, 0x05, 0x06, 0x07, 0x08};

// void send_midi_note(uint8_t note, bool on) {
//     uint8_t msg[] = { (on ? 0x90 : 0x80), note, (on ? 100 : 0) };
//     tud_midi_stream_write(0, msg, 3);
// }

// void send_hid_key(uint8_t keycode) {
//     if (!tud_hid_ready()) return;

//     uint8_t report[6] = {0};
//     report[0] = keycode;
//     tud_hid_keyboard_report(0, 0, report);
//     sleep_ms(10);
//     tud_hid_keyboard_report(0, 0, NULL); // Release
// }

// int main() {
//     board_init();
//     tusb_init();
//     gpio_driver_init(); // new

//     bool last_state[NUM_KEYS] = {false};

//     while (true) {
//         tud_task();

//         for (int i = 0; i < NUM_KEYS; ++i) {
//             bool pressed = gpio_read(gpio_key_pins[i]);

//             if (pressed && !last_state[i]) {
//                 send_midi_note(midi_notes[i], true);
//                 send_hid_key(hid_keycodes[i]);
//                 last_state[i] = true;
//             } else if (!pressed && last_state[i]) {
//                 send_midi_note(midi_notes[i], false);
//                 last_state[i] = false;
//             }
//         }

//         sleep_ms(10);
//     }

//     return 0;
// }

#include "bsp/board.h"
#include "tusb.h"

void send_test_key() {
    if (!tud_hid_ready()) return;

    uint8_t keycode[6] = {0x04}; // 'A' key
    tud_hid_keyboard_report(0, 0, keycode);
    sleep_ms(100);
    tud_hid_keyboard_report(0, 0, NULL); // release
}

int main() {
    board_init();
    tusb_init();

    while (true) {
        tud_task();
        send_test_key();
        sleep_ms(2000);
    }
}