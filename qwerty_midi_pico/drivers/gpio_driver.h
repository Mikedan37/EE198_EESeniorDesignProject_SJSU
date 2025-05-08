#ifndef GPIO_DRIVER_H
#define GPIO_DRIVER_H

#include "pico/stdlib.h"

#define NUM_KEYS 5
extern const uint gpio_key_pins[NUM_KEYS];

void gpio_driver_init();
int gpio_read(uint8_t pin);

#endif