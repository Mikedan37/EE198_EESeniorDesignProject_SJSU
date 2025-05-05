#pragma once
#include <stdint.h>   // <-- Make sure this is included

void gpio_init(void);
int gpio_read(uint8_t pin);  // ✅ Fix this line