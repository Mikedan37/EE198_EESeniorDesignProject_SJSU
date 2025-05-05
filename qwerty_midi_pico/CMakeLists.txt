cmake_minimum_required(VERSION 3.13)
include(pico_sdk_import.cmake)

project(qwerty_midi_pico)

pico_sdk_init()

add_executable(qwerty_midi_pico
    main.c
    usb_descriptors.c
)

target_include_directories(qwerty_midi_pico PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries(qwerty_midi_pico pico_stdlib tinyusb_device tinyusb_board)

pico_add_extra_outputs(qwerty_midi_pico)