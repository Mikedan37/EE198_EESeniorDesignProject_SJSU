🥁 USB Powered Single Octave MIDI & QWERTY Keyboard 🎹

🚀 An open-source MIDI & QWERTY keyboard framework with a plug-and-play driver, supporting dynamic device detection, USB-HID, and MIDI communication.

📜 Project Overview

This project is an open-source plug-and-play framework and driver for MIDI and QWERTY keyboards, allowing seamless integration of typing and musical input. Our goal is to develop a cross-platform system that enables automatic device recognition and configuration upon connection.

🎯 Key Features:
	•	Dual Keyboard Support: Handles both MIDI and QWERTY keyboards.
	•	Plug-and-Play: Automatic detection and configuration without manual setup.
	•	USB-HID & MIDI Compatibility: Processes standard keyboard input and MIDI signals.
	•	Mode Switching Logic: Enables smooth transitions between typing and musical input.
	•	Cross-Platform API: Supports Mac, Windows, and Linux for key remapping and MIDI customization.

🛠️ Hardware Architecture

🎛️ Hardware Components
	•	Microcontroller: Raspberry Pi Pico (RP2040) for prototyping.
	•	Custom PCB Design: Supports USB-C, I²C, or SPI interfaces.
	•	Keyboard Matrix & Input Handling: Efficiently scans and processes key presses.

🔌 Firmware & Driver Development
	•	Dynamic Device Detection: Identifies MIDI or QWERTY mode automatically.
	•	Low-Latency Processing: Optimized firmware for minimal input lag.
	•	USB Communication: Implements HID for QWERTY input and MIDI for note processing.

💻 Software & API
	•	Device Configuration App: Allows users to remap keys and modify MIDI settings.
	•	Firmware Updates: Supports future expansions such as Bluetooth MIDI integration.
	•	Hot-Swapping: Detects device connections and updates configurations in real time.

🚀 Getting Started

🔧 Prerequisites
	1.	Install Python 3.8+ and required libraries:

pip install pyusb numpy hidapi


	2.	Install PlatformIO for firmware development:

pip install platformio


	3.	Clone the repository:

git clone https://github.com/your-repo/midi-qwerty-keyboard.git
cd midi-qwerty-keyboard



📦 Hardware Setup
	•	Connect the MIDI/QWERTY keyboard to your computer via USB.
	•	If using the Raspberry Pi Pico, flash the firmware using:

pio run --target upload


	•	Verify device detection using:

lsusb



🎼 Usage
	1.	Plug in the keyboard – the driver automatically detects the device.
	2.	Launch the configuration app to remap keys or adjust MIDI settings.
	3.	Play or type seamlessly – switch between modes without manual intervention.

📌 Roadmap
	•	Develop keyboard matrix scanning
	•	Implement USB-HID & MIDI communication
	•	Design and manufacture custom PCBs
	•	Optimize driver performance
	•	Release open-source API for customization

🤝 Contributing

Want to contribute? Fork the repo and submit a pull request! 🚀
	1.	Fork the repository on GitHub.
	2.	Create a new branch for your feature:

git checkout -b feature-name


	3.	Commit your changes and push to your branch:

git commit -m "Added new feature"
git push origin feature-name


	4.	Submit a pull request and describe your changes.

📜 License

This project is licensed under the MIT License. See LICENSE for details.

📬 Contact

👨‍💻 Developers:
	•	Michael Dany – Software Development & API Design
	•	Christopher “Zac” Hatchett – Digital Logic & Hardware Design

📧 Reach out via email for collaboration opportunities!
