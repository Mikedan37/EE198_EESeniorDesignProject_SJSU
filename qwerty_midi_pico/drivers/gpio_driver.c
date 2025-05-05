#include "gpio_driver.h"
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

// This fake state changes every second like a pressed key
static int fake_pin_states[32] = {0};
static uint32_t last_toggle = 0;
static int active_pin = 0;

void gpio_init() {
    last_toggle = time(NULL);
    srand(time(NULL));
}

int gpio_read(uint8_t pin) {
    uint32_t now = time(NULL);
    if (now != last_toggle) {
        last_toggle = now;
        active_pin = rand() % 24;
    }
    return pin == active_pin; // Only one active at a time
}