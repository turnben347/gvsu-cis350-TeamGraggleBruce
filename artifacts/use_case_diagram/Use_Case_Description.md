# Use Case Description: **Change Light Color**

---

### **Use Case Name**: Change Light Color

### **Use Case ID**: UC3

### **Actor**:  
- **Primary Actor**: User

### **Stakeholders and Interests**:
- **User**: Wants to easily change the light's color using an intuitive interface, with minimal effort.
- **System Admin**: Ensures that the light responds accurately to the user's input.
- **Manufacturer**: Ensures the smart light operates seamlessly and interacts with the system correctly.
  
---

### **Preconditions**:
- The system is powered on and running.
- The smart light device is connected to the system and available for control.
- The user is authenticated and logged into the app.
- The app is communicating successfully with the light through the `pythonkasa` library (FR12).

### **Postconditions**:
- **Success**: The color of the smart light has been successfully changed to the user's selected option.
- **Failure**: The system shows an error message, and the light’s color remains unchanged.

---

### **Main Success Scenario (Basic Flow)**:

1. **User Action**: The user opens the application and navigates to the control panel of the smart light.
2. **System Response**: The app displays the current light settings, including the current color.
3. **User Action**: The user clicks on the "Change Color" button.
4. **System Response**: The app displays a color picker (FR3), offering options to choose a custom color or one of the preset colors (FR7).
5. **User Action**: The user selects a color using the color picker.
6. **System Response**: The system sends an API request to the smart light via the `pythonkasa` library to change the light color (FR3, FR12).
7. **System Response**: The system updates the display to reflect the new light color.
8. **System Response**: The system provides confirmation that the light color was successfully changed, within 1 second of input (NFR1).

---

### **Extensions (Alternative Flows)**:

#### **Flow A: Network Failure**

- **Trigger**: The network connection is lost.
  - **1a. System Response**: The system displays the current network status indicator as disconnected (FR10).
  - **1b. System Response**: The system disables the color picker and displays a message that the smart light is inaccessible (FR9).
  - **1c. End**: The user cannot change the light color until the network connection is restored.

#### **Flow B: User Cancels Color Change**

- **Trigger**: The user decides not to change the light color.
  - **4a. User Action**: The user clicks "Cancel" instead of selecting a color from the color picker.
  - **4b. System Response**: The system closes the color picker and retains the current light color.
  - **4c. End**: No further actions occur, and the use case ends.

---

### **Special Requirements**:
- The system should be visually appealing and user-friendly, with an intuitive and modern design for the color picker (NFR2).
- The interface must make all color-changing actions easily accessible within two clicks (NFR3).
- The action must have a response time of under 1 second (NFR1).
- The app should utilize minimal system resources, ensuring performance even on low-end devices (NFR5).

---

### **Trigger**:
- The user wants to change the color of the smart light manually.

---

### **Assumptions**:
- The user is familiar with the app and knows how to use the color picker.
- The smart light is compatible with the app and can handle color changes.

### **Requirements Linked**:
- **Functional Requirements**: FR3, FR7, FR9, FR10, FR12
- **Non-Functional Requirements**: NFR1, NFR2, NFR3, NFR5
