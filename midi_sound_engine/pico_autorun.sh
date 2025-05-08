#!/bin/bash

# Check if the Pico is connected
if system_profiler SPUSBDataType | grep -q "RP2040"; then
    echo "🎹 Pico detected — launching synth!"
    cd ~/path/to/midi_sound_engine  # Change this to your actual path
    /usr/bin/python3 unified_listener.py
else
    echo "❌ Pico not found."
fi