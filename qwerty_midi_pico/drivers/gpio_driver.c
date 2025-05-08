#include "gpio_driver.h"
#include "pico/stdlib.h"

// Define which GPIOs are used for keys
const uint gpio_key_pins[NUM_KEYS] = {0, 1, 2, 3, 4};

void gpio_driver_init() {
    for (int i = 0; i < NUM_KEYS; ++i) {
        gpio_init(gpio_key_pins[i]);
        gpio_set_dir(gpio_key_pins[i], GPIO_IN);
        gpio_pull_down(gpio_key_pins[i]);  // ✅ correct for pull-down config
    }
}

int gpio_read(uint8_t pin) {
    return gpio_get(pin);  // HIGH = pressed with pull-down
}