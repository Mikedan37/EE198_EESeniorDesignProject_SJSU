#ifndef GPIO_DRIVER_H
#define GPIO_DRIVER_H

#include "pico/stdlib.h"

#define NUM_KEYS 5
extern const uint gpio_key_pins[NUM_KEYS];

void gpio_driver_init();
void gpio_poll_keys(); // To be called repeatedly or on a thread
bool gpio_is_pressed(uint8_t pin); // Query current state

#endif