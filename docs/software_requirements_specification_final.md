# Overview
This Software Requirements Specification document outlines the functional and non-functional requirements for a Python-based GUI application designed to control a smart light using a Python library. It describes how the system will allow users to turn the light on or off, adjust brightness, and change colors. Additionally, this document covers performance expectations, such as response time, usability, and reliability. The purpose of this document is to define the complete functionality and performance for the development, testing, and maintenance of the system.
# Functional Requirements
# Light Management Features
- FR1: Turn Light On: The system shall provide a button to turn the smart light on.
- FR2: Turn Light Off: The system shall provide a button to turn the smart light off.
- FR3: Change Light Color: The system shall allow the user to change the color of the light through a color picker.
- FR4: Adjust Brightness: The system shall provide a slider for the user to adjust the brightness of the light.
- FR5: The system shall update the light color in real-time when a new color is selected.
# Advanced Settings and Customization
- FR6: The system shall provide a button to toggle the light's state (ON/OFF) and dynamically update its label to reflect the light's current status.
- FR7: Light Color Presets: The system shall provide preset color options that the user can select to change the light color quickly.
- FR8: The system shall automatically adjust brightness to a minimum threshold of 1%.
- FR9: The system shall cancel previously scheduled brightness updates when the slider is moved, ensuring smooth transitions.
- FR10: The system shall implement a delay to optimize brightness updates for smoother user interaction.
# System Requirements
- FR11: Python as the Programming Language: The system shall be implemented using Python as the primary language.
- FR12: Use of the pythonkasa Library: The system shall utilize the pythonkasa library to communicate with TP-Link smart lights.
- FR13: Graphical User Interface Library: The system shall use a Python GUI to create a user-friendly interface.
- FR14: Windows 10 Compatibility: The system shall be fully compatible with Windows 10.
- FR15: Standalone App: The final app shall be able to run standalone.

# Non-Functional Requirements
# Performance
1. NFR1: Response Time: The system shall respond to user input within 1 second.
2. NFR2: Startup Time: The system shall load and become fully functional within 5 seconds of being launched.
3. NFR3: Storage Size: The app shall not take up more than 500MB.
4. NFR4: Resource Usage: The system shall use minimal system resources, ensuring it can run efficiently on low-end machines.
5. NFR5: Reliability: The system shall perform interactions reliably, with a failure rate of less than 1%.
# Usability
6. NFR6: User Interface: The GUI shall be intuitive with a imple and clean design.
7. NFR7: Usability: The system shall be easy to use, with all major actions accessible within two clicks.
8. NFR8: Screen Size: The app GUI shall not take up for than 1/4 of the screen.
9. NFR9: Simplicity: The app shall be simple looking and easy to use with less than 10 buttons on the screen.
10. NFR10: UI: All UI components shall be accessible via mouse interaction.
Scalability/Maintainability:
11. NFR11: Maintainability: The code shall follow coding best practices to allow for easy maintenance and updates.
12. NFR12: IP Control: The code shall allow for easy IP address assignment to control additional smart bulbs in the future.
13. NFR13: Modularity: The code shall be modular, separating GUI logic, bulb control, and other functions to allow easier updates.
14. NFR14: Best Coding Practices: The application shall use a consistent naming convention for all variables, functions, and classes to improve readability and maintainability.
15. NFR15: Expansion: The system shall allow for easy expansion to support multiple bulbs in the future by modifying the codebase with minimal changes.
