# Overview
This Software Requirements Specification document outlines the functional and non-functional requirements for a Python-based GUI application designed to control a smart light using an API. It describes how the system will allow users to turn the light on or off, adjust brightness, change colors, and schedule on/off times. Additionally, this document covers performance expectations, such as response time, usability, and reliability. The purpose of this document is to define the complete functionality and performance for the development, testing, and maintenance of the system.
# Functional Requirements
1. FR1: Turn Light On: The system shall provide a button to turn the smart light on via an API call.
2. FR2: Turn Light Off: The system shall provide a button to turn the smart light off via an API call.
3. FR3: Change Light Color: The system shall allow the user to change the color of the light through a color picker.
4. FR4: Adjust Brightness: The system shall provide a slider for the user to adjust the brightness of the light.
5. FR5: Schedule Light On: The system shall allow the user to schedule a time for the light to automatically turn on.
6. FR6: Schedule Light Off: The system shall allow the user to schedule a time for the light to automatically turn off.
7. FR7: Light Color Presets: The system shall provide preset color options that the user can select to change the light color quickly.
8. FR8: Reset Light to Default Settings: The system shall provide a button to reset the light settings to default.
9. FR9: Availability: The system shall be available for use without an outside internet connection.
10. FR10: Status Indicator: The system shall display the current network status so the user knows whether the light can be accessed.
11. FR11: Python as the Programming Language: The system shall be implemented using Python as the only programming language.
12. FR12: Use of the pythonkasa Library: The system shall utilize the pythonkasa library to communicate with TP-Link smart device.
13. FR13: Graphical User Interface Library: The system shall use a Python GUI to create a user-friendly interface.
14. FR14: Windows 10 Compatibility: The system shall be fully compatible with Windows 10.
15. FR15: Standalone App: The app shall be able to run standalone.

# Non-Functional Requirements
1. NFR1: Response Time: The system shall respond to user input within 1 second.
2. NFR2: User Interface Aesthetics: The GUI shall be intuitive and visually appealing, with a modern and clean design.
3. NFR3: Usability: The system shall be easy to use, with all major actions accessible within two clicks.
4. NFR4: Reliability: The system shall perform interactions reliably, with a failure rate of less than 1%.
5. NFR5: Resource Usage: The system shall use minimal system resources, ensuring it can run efficiently on low-end machines.
6. NFR6: Maintainability: The code shall follow coding best practices to allow for easy maintenance and updates.
7. NFR7: Startup Time: The system shall load and become fully functional within 5 seconds of being launched.
8. NFR8: Screen Size: The app GUI shall not take up for than 1/4 of the screen.
9. NFR9: Storage Size: The app shall not take up more than 500MB.
10. NFR10: Simplicity: The app shall be simple looking and easy to use with less than 10 buttons on the screen.
