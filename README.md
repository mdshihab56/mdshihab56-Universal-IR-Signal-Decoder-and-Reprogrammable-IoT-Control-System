# Abstract
Infrared (IR) communication is widely used for consumer electronics, but proprietary, device-specific systems limit universal control and interoperability. This project presents a Universal IR Signal Decoder and Reprogrammable IoT Control System using an Arduino Uno, a VS1838B receiver, and a 16x2 I2C LCD. The system captures, decodes, and visualizes hexadecimal commands and signal timings in real time. Experimental analysis confirms successful multi-device decoding, establishing a foundational framework for future loT integration, protocol reverse engineering, and machine learning-based smart-home automation.

## 1. Introduction
Infrared communication technology has been extensively used in consumer electronics due to its simplicity, low power consumption, and cost efficiency. Most traditional remote control systems rely on encoded IR pulse sequences transmitted through infrared LEDs and received by IR sensors integrated into electronic devices. Despite widespread adoption, existing remote control ecosystems suffer from several limitations:
1. Device-specific communication protocols
11. Lack of interoperability
III. Limited customization
IV. Incompatibility across manufacturers
V. Difficulty in reverse engineering unsupported devices

Modern smart home systems increasingly demand universal compatibility and programmable interfaces capable of interacting with diverse hardware platforms. Therefore, the development of an adaptive IR signal acquisition and decoding system is essential for enabling next-generation IoT automation and embedded control systems. This project focuses on the development of a low-cost, real-time IR signal analyzer capable of:
1. Capturing IR pulses
11. Extracting hexadecimal command data
III. Measuring signal delay intervals
IV. Displaying decoded information
V. Providing a foundation for universal IR control systems

## 2. Research Motivation
Most consumer devices use proprietary IR protocols, preventing users from easily modifying, integrating, or automating hardware systems. Existing universal remotes are often limited to predefined device databases and cannot dynamically learn or analyze unknown protocols. The motivation behind this research includes:
1. Understanding embedded IR communication systems
11. Building a universal remote learning platform
III. Supporting smart-home automation
IV. Enabling low-cost reverse engineering research
V. Developing adaptive IoT interfaces
VI. Exploring machine learning applications in signal classification

This system provides a practical and scalable solution for experimenting with infrared-based communication systems in both academic and industrial environments.

## 3. Objectives
The primary objectives of this project are:
1. Universal Decoding: Design an adaptable interface to decode signals across diverse manufacturer protocols.
II. Data Extraction: Capture real-time hexadecimal command values and analyze signal transmission intervals.
III. Live Visualization: Present decoded data directly onto a physical LCD interface.
IV. IoT & Al Foundation: Establish a scalable groundwork for future reprogrammable remote mapping and smart Al integration.

## 4. Hardware Components
| Component | Description |
| :--- | :--- |
| Arduino Uno | Main microcontroller platform |
| VS1838B IR Receiver | Receives infrared signals |
| 16x2 I2C LCD | Displays decoded information |
| Passive Buzzer | Audio feedback for signal detection |
| Remote Controls | IR signal source |
| Jumper Wires | Circuit connections |
| Breadboard | Prototyping platform |

## 5. Software Environment
| Software | Purpose |
| :--- | :--- |
| Arduino IDE | Firmware programming |
| IR-remote | IR decoding |
| Python | Data analysis and graph generation |
| Matplotlib | Graph plotting |
| Pandas | Data processing |
| draw.io | System architecture diagrams |

## 6. System Architecture
The proposed system follows a modular embedded architecture.

Remote Control
↓
IR Signal Transmission
↓
VS1838B IR Receiver
↓
Arduino Uno
↓
IR Signal Decoding
↓
HEX Value Extraction
↓
Delay Analysis
↓
LCD Visualization
↓
Serial Monitor Logging
↓
Future IoT Device Mapping

## 7. Working Principle
The IR receiver continuously monitors incoming infrared pulse sequences emitted by remote controls. When a signal is detected, the microcontroller processes the encoded pulse timings using the IRremote library. The decoded signal is then:
1. Converted into hexadecimal format
2. Displayed on the LCD
3. Logged to the serial monitor
4. Time-stamped for delay analysis
5. Used for future device mapping possibilities

A buzzer provides immediate audio feedback whenever a signal is successfully detected.

## 8. Methodology
1. Signal Acquisition: The VS1838B sensor intercepts incoming modulated IR pulses from the target remote control.
2. Protocol Decoding: The underlying firmware utilizes the IR-remote library to parse the raw pulse sequences into standardized hexadecimal values.
3. Timing Evaluation: The system tracks execution intervals and transmission delays using Arduino's built-in millis() function.
4. Local Display: The extracted HEX codes and timing metrics are instantly formatted and written to the 16x2 I2C LCD.
5. Serial Logging: Simultaneously, the data is piped to the Serial Monitor to allow for live debugging and data collection.

## 9. Arduino Implementation
The implemented firmware performs:
1. Real-time IR signal detection
11. HEX code extraction
III. Timing interval measurement
IV. LCD visualization
V. Audio feedback generation

Main features of the implementation include:
1. Efficient real-time processing
11. Low hardware complexity
III. Portable embedded architecture
IV. Expandable universal control capability

## 10. Experimental Analysis
Multiple remote controls were tested to evaluate:
1. Signal detection reliability
II. Decoding consistency
III. Timing behavior
IV. Multi-device compatibility

The system successfully decoded signals from several consumer electronic devices.

## 11. Graphical Analysis
* IR Signal Pulse Waveform
<img width="1920" height="975" alt="IR Signal Pulse Waveform" src="https://github.com/user-attachments/assets/af4c1250-a22c-4ed9-8509-3a92691b26bf" />

* IR Signal Decoding Delay
<img width="1920" height="975" alt="IR Signal Decoding Delay" src="https://github.com/user-attachments/assets/0487a2d6-8bef-48d5-8f79-d20045c1be3b" />

* Multi-Device IR Protocol Detection Accuracy
<img width="1920" height="975" alt="Multi device ir protocol detection accuracy" src="https://github.com/user-attachments/assets/999d3d14-3649-4240-bcaa-015d7d2b2304" />

* IR Pulse Duration Distribution
<img width="1920" height="975" alt="pulse duration" src="https://github.com/user-attachments/assets/b3f3d0ce-3de9-40dd-afb3-e2cced98dc65" />

* IR Pulse Width Distribution
<img width="1920" height="975" alt="IR Pulse Width Distribution" src="https://github.com/user-attachments/assets/8152302b-0784-4aa6-ad53-becf756fa254" />

## 12. Limitations
I. Line-of-Sight & Range: Requires a direct path between the remote and the VS1838B receiver, with performance dropping over longer distances or sharp angles.
II. Protocol Constraints: Non-standard or highly complex proprietary protocols may decode as "unknown" or return inconsistent HEX values.
III. Environmental Noise: Ambient IR interference can distort raw pulse sequences and affect timing accuracy.
IV. Hardware Memory Limits: The Arduino Uno's ATmega328P microcontroller has limited SRAM, restricting the ability to store large multi-device lookup databases directly on the chip.

## 13. Conclusion
This project successfully implemented a low-cost, real-time Universal IR Signal Decoder using an Arduino Uno, a VS1838B receiver, and an I2C LCD. The system reliably captured modulated IR pulses, extracted hexadecimal command values, and measured transmission timing intervals across various consumer remotes. By providing an open, modular framework to bypass proprietary device barriers, this architecture establishes a practical foundation for future universal remote mapping, machine learning-based signal analysis, and smart loT automation.
