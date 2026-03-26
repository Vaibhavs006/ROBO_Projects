# ROBO_Projects 🤖

A collection of robotics projects exploring microcontroller programming and embedded systems. This repository documents my journey as a 2nd-year engineering student learning robotics, motor control, and IoT applications.

## Overview

This project repository contains practical implementations of robotics concepts including:
- **Motor Control Systems** - PWM-based motor speed and direction control
- **Microcontroller Integration** - ESP32 and Raspberry Pi implementations
- **Embedded Programming** - Real-time system control and sensor interfacing

## Project Structure

```
ROBO_Projects/
├── ESP32_BTS7960.ino       # ESP32 motor driver integration
├── RASPI.py                # Raspberry Pi control scripts
└── README.md               # This file
```

## Technologies Used

| Technology | Usage | Purpose |
|-----------|-------|---------|
| **ESP32** | Microcontroller | Real-time motor control & PWM generation |
| **Raspberry Pi** | Single Board Computer | High-level control & automation |
| **BTS7960** | Motor Driver | Bidirectional DC motor control |
| **Python** | Programming | Robot control logic & automation |
| **C++** | Programming | Low-level microcontroller operations |

## Key Projects

### 1. ESP32 Motor Control (ESP32_BTS7960.ino)
**Purpose:** Control DC motors using ESP32 microcontroller with BTS7960 motor driver

**Features:**
- PWM-based speed control
- Bidirectional motor rotation (forward/reverse)
- Real-time response to input signals
- Hardware compatibility with BTS7960 module

**Hardware Requirements:**
- ESP32 Development Board
- BTS7960 Motor Driver Module
- DC Motor(s)
- Power Supply (12V recommended)
- Jumper wires & breadboard

**Connections:**
```
ESP32 Pin Configuration:
- GPIO 25, 26 → BTS7960 Input Pins (IN1, IN2)
- GPIO 12, 13 → PWM Control Pins
- GND → Common Ground
```

### 2. Raspberry Pi Controller (RASPI.py)
**Purpose:** High-level robot control and automation using Python

**Features:**
- GPIO-based device control
- Sensor data processing
- Automated decision making
- Serial communication with ESP32

**Requirements:**
```bash
pip install RPi.GPIO
```

**Basic Usage:**
```python
import RPi.GPIO as GPIO
# Control logic implementation
```

## Getting Started

### Prerequisites
- Python 3.7+ (for Raspberry Pi scripts)
- Arduino IDE or PlatformIO (for ESP32 code)
- Git for version control

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/Vaibhavs006/ROBO_Projects.git
cd ROBO_Projects
```

2. **For ESP32 Development:**
   - Install Arduino IDE or PlatformIO
   - Add ESP32 board support
   - Open `ESP32_BTS7960.ino` and configure pins as needed
   - Upload to your ESP32 board

3. **For Raspberry Pi:**
   - Install Python dependencies:
   ```bash
   pip install -r requirements.txt  # (if available)
   ```
   - Run the control script:
   ```bash
   python RASPI.py
   ```

## Learning Outcomes

Through these projects, I'm learning:
- ✅ Microcontroller programming & hardware interfacing
- ✅ PWM signals & motor control techniques
- ✅ GPIO manipulation & embedded systems concepts
- ✅ Serial communication protocols
- ✅ Python for embedded systems
- ✅ Circuit design & electronics basics


## References & Learning Resources

**Official Documentation:**
- [ESP32 Arduino Core](https://docs.espressif.com/projects/arduino-esp32/)
- [Raspberry Pi GPIO Documentation](https://www.raspberrypi.org/documentation/usage/gpio/)

**Tutorials:**
- PWM Motor Control concepts
- BTS7960 Module datasheet
- GPIO interfacing guides


## Contributing

As a learning project, I welcome suggestions! Feel free to:
- Report issues or bugs
- Suggest improvements
- Share optimizations
- Contribute additional projects

## License

This project is open source. Feel free to use, modify, and distribute as needed for educational purposes.

## Author

**Vaibhavs006** - Engineering Student (2nd Year)
- Exploring robotics 
- Learning microcontroller programming
- Passionate about hands-on projects

---

**Got Questions?**
Feel free to open an issue or reach out with questions about the projects, setup, or concepts!

