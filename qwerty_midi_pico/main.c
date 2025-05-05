#include "pico/stdlib.h"
#include "bsp/board.h"
#include "tusb.h"

// Simulated keys: A, B, C, D
const uint8_t test_keys[] = {0x04, 0x05, 0x06, 0x07};

void send_keypress(uint8_t keycode) {
    if (!tud_hid_ready()) return;

    uint8_t report[6] = {0};
    report[0] = keycode;
    tud_hid_keyboard_report(0, 0, report);
    sleep_ms(10);
    tud_hid_keyboard_report(0, 0, NULL); // Release
}

void fake_button_input() {
    static uint32_t last_sent = 0;
    static int key_index = 0;
    uint32_t now = board_millis();

    if (now - last_sent > 1000) {
        send_keypress(test_keys[key_index]);
        key_index = (key_index + 1) % 4;
        last_sent = now;
    }
}

int main() {
    board_init();
    tusb_init();

    while (1) {
        tud_task();
        fake_button_input();  // 🔁 Replace this with GPIO check later
    }
}