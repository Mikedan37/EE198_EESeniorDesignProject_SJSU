#include "gpio_driver.h"
#include "pico/multicore.h"
#include <stdio.h>

const uint gpio_key_pins[NUM_KEYS] = {0, 1, 2, 3, 4};
static bool key_state[NUM_KEYS] = {false};
static bool prev_key_state[NUM_KEYS] = {false};

void gpio_driver_init() {
    for (int i = 0; i < NUM_KEYS; ++i) {
        gpio_init(gpio_key_pins[i]);
        gpio_set_dir(gpio_key_pins[i], GPIO_IN);
        gpio_pull_down(gpio_key_pins[i]);
    }
}

// Background polling loop for Core 1
void gpio_poll_loop() {
    while (true) {
        for (int i = 0; i < NUM_KEYS; ++i) {
            bool current = gpio_get(gpio_key_pins[i]);

            if (current && !prev_key_state[i]) {
                printf("Note ON: %d\n", i); // You can replace this with event queuing
            } else if (!current && prev_key_state[i]) {
                printf("Note OFF: %d\n", i);
            }

            prev_key_state[i] = current;
            key_state[i] = current;
        }
        sleep_ms(5);
    }
}

bool gpio_is_pressed(uint8_t pin) {
    return (pin < NUM_KEYS) ? key_state[pin] : false;
}