#pragma once
#include <stdint.h>

#define NUM_KEYS 4

const uint8_t key_pins[NUM_KEYS] = {2, 3, 4, 5};
const uint8_t qwerty_keymap[NUM_KEYS] = {
    0x04,  // A
    0x05,  // B
    0x06,  // C
    0x07   // D
};