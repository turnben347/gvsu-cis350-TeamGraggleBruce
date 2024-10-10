# Overview
This Software Requirements Specification (SRS) document outlines the functional and non-functional requirements for a Python-based GUI application designed to control a smart light using an API. It describes how the system will allow users to turn the light on or off, adjust brightness, change colors, and schedule on/off times. Additionally, this document covers performance expectations, such as response time, usability, and reliability. The purpose of this document is to define the complete functionality and performance for the development, testing, and maintenance of the system.
# Functional Requirements
1. FR1: Turn Light On: The system shall provide a button to turn the smart light on via an API call.
2. FR2: Turn Light Off: The system shall provide a button to turn the smart light off via an API call.
3. FR3: Change Light Color: The system shall allow the user to change the color of the light through a color picker.
4. FR4: Adjust Brightness: The system shall provide a slider for the user to adjust the brightness of the light.
5. FR5: Schedule Light On: The system shall allow the user to schedule a time for the light to automatically turn on.
6. FR6: Schedule Light Off
The system shall allow the user to schedule a time for the light to automatically turn off.

# Non-Functional Requirements
1. NFR1: Response Time: The system shall respond to user input (such as button clicks or slider adjustments) within 1 second.
2. NFR2: Availability: The system shall be available for use without an outside internet connection
3. NFR4: User Interface Aesthetics: The GUI shall be intuitive and visually appealing, with a modern and clean design.
4. NFR5: Usability: The system shall be easy to use, with all major actions (on/off, brightness, color change) accessible within two clicks.
5. NFR9: Reliability: The system shall perform API interactions reliably, with a failure rate of less than 1% for all API calls.
6. NFR10: Minimal Resource Usage: The system shall use minimal system resources (CPU and memory), ensuring it can run efficiently on low-end machines.
7. NFR17: Maintainability: The codebase shall follow clear coding standards and best practices to allow for easy maintenance and updates.
8. 
