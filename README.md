```
Introduction to Software Engineering - CIS 350
```

### SmartLight: A Desktop GUI Smart Light Control App

---
### Made by:
#### Adam Kroese (Project Manager)
#### Ben Turner (Lead Programmer)
---
## 1 Abstract

With the growing trend of mobile applications abandoning support for smart-home devices, users are left without reliable control over their connected homes. This project addresses this issue by developing a robust desktop application designed to ensure long-term control over smart-home lighting systems, independent of third-party apps that may lose support in the future. Our solution focuses on creating a user-friendly interface that allows seamless control over smart-home lights, offering features such as brightness adjustment and color changes. By eliminating the reliance on volatile mobile apps, this desktop application provides a stable and future-proof platform, empowering users to manage their smart-home lighting systems efficiently and with confidence for years to come.

## 2 Introduction

In recent years, smart-home devices have become integral to modern living, offering convenience and control over various household systems. However, many users face the challenge of mobile applications suddenly abandoning support for these devices, leaving them without a reliable way to manage their homes. This project seeks to solve that problem by developing a desktop application specifically designed for controlling smart-home lighting systems. Unlike mobile apps that can lose support or functionality over time, this desktop solution offers a future-proof alternative, ensuring continuous control and accessibility for users. Our goal is to provide a stable and long-lasting application that does not depend on third-party developers or evolving app stores. The desktop app allows users to control their smart-home lights with ease, offering features such as on/off control, brightness adjustment, and color customization. With its intuitive interface and focus on longevity, this app empowers users to confidently manage their smart-home lighting systems, knowing their control will not be interrupted by unsupported mobile apps. This solution will benefit those seeking reliable, long-term smart-home management, offering an accessible and durable platform.

### 2.1 Trello

We used Trello to manage tasks and track progress throughout the project. Trello helped us break down the project into manageable tasks to be done one at a time. It allowed us to prioritize each task one by one in order to track issues and address problems as we worked on it. Overall, Trello kept our team and project itself organized and on track, ensuring we met all of our project goals.

https://trello.com/invite/b/67059692952ac4f37df16a01/ATTI3b5840917eb7dd9c7e9df87764a464295DC070C2/smartlightapp

## 3 Architectural Design

### 3.1 Use Case Diagram

In a use case diagram for a this SmartLight app, the primary actor is the User who interacts with functionalities like controlling the Smart-Home light by turning it on/off, asjuting the brightness, and changing the color. While the Smart-Home system or light itself, covers the same functionalities that the user interacts with. This diagram outlines the essential interactions and functionalities between the user and the Smart-Home system.

<p align="center">
  <img src="artifacts/use_case_diagram/UseCase.png" width="500" title="use case diagram">
  <br>
  <br>
  Figure 1: Use Case Diagram

  ### 3.2 Class Diagram

  This section includes a class diagram for the SmartLight application. The diagram highlights the following components:

- **Boundary Class**: SmartLightApp
- **Control Class**: SmartLightController
- **Entity Classes**: SmartLight, Slider, ColorPicker, Color

This diagram demonstrates how the user interface, control logic, and device models interact within the SmartLight application. It offers a clear view of how these components work together to manage light control, adjust brightness, and change colors.

<p align="center">
  <img src="artifacts/Class.png" width="500" title="class diagram">
  <br>
  <br>
  Figure 2: Class Diagram
</p>

### 3.3 Sequence Diagram

This section contains the sequence diagram for a user interacting with the smart light app. The user starts by toggling the light on or off, adjusting the brightness using the slider, and selecting a color through the color picker. The app processes these inputs, communicates with the smart light, and updates the user interface to reflect the changes.

<p align="center">
  <img src="artifacts/Sequence.png" width="500" title="sequence diagram">
  <br>
  <br>
  Figure 3: Sequence Diagram
</p>

## 4 User Guide/implementation

### 4.1 Client Side

#### 4.1.1 Starting the Application

Using a python IDE, copy and the code python code provided in the src file and make sure to change the IP address to the location of your "tp-link Kasa Smart Light Bulb: Multicolor". Also make sure your device and light are on the same wifi network. The user then needs to make the sure the light is turned on and then run the code in the IDE. (To make using this code easier going forward, make the code into an .exe file and it works the same without having to use an IDE. Keep in mind the .exe file only works for the current IP address of the light, so if you change the code at all, you have to make a new .exe). When the code is working properly, the the app will open to the Home Screen.

### 4.2 Home

From this window the user can turn the light on and off, change the brightenss from 0 to 100 using a slider, or change the color.

<p align="center">
  <img src="artifacts/HomeScreen.png" width="175
  " title="App Screen">
  <br>
  <br>
  Figure 4: Home Sceen
</p>

<p align="center">
  <img src="artifacts/HomeScreen2.png" width="175
  " title="App Screen 2">
  <br>
  <br>
  Figure 5: Home Sceen (100 brightness w/ light turned on)
</p>

### 4.3 Color Picker

When the user clicks on the "Change Color" button, it opens a popup window with a color picker that includes a wide range of pre-selected colors along with the option to type in RGB values.

<p align="center">
  <img src="artifacts/ColorPicker.png" width="300
  " title="Color Picker">
  <br>
  <br>
  Figure 6: Color Picker
</p>

## 5 Risk Analysis and Retrospective

At the start of the project, we were ambitious with our goals, but the limited time available posed a challenge. One of the primary risks was implementing all the desired features within the deadline, particularly due to the complexity of integrating various functionalities for controlling the lights. A recurring issue was ensuring that changes made by the user (such as turning the light on/off, adjusting brightness, or changing color) were applied correctly to the right light. Additionally, we faced difficulties getting the scheduling function down, which is why we decided to scrap that feature entirely in the final version. To overcome these challenges, we used various online resources to troubleshoot specific issues and find solutions. This approach allowed us to effectively address technical problems and maintain progress in the development process. Despite these obstacles, we successfully implemented several key features. Users can now turn their lights on/off, adjust brightness, and change colors, with the changes applied immediately to the corresponding light. And We tried our best to ensure that these interactions are smooth which they ended up being.
One area that could have been improved is the user interface. The UI ended up feeling very plain and boring and If we had more time to focus on UI design, we could have created a more cohesive and user-friendly experience, making the app even more efficient and pleasant for users.

## 6 Future Scope

There are several enhancements we could incorporate into future versions of the SmartLight app to improve both user experience and functionality. One of the key features we could introduce is the ability to save and recall lighting preferences. This will allow users to easily set their preferred brightness and color schemes for different times of the day or moods, ensuring a more personalized and seamless experience. Additionally, we could plan to revisit our failed scheduling function. It would give the ability to set schedules for lights to automatically turn on/off, adjust brightness, or change color at specific times. This will improve convenience for users and help optimize energy usage, providing a more automated and efficient experience. 

## 7 Conclusion

Overall, the SmartLight app provides essential tools for anyone looking to control and personalize their smart-home lighting experience. By allowing users to turn lights on/off, adjust brightness, and change colors, we aim to make home lighting more convenient, customizable, and enjoyable. We believe this app has the potential to be a great option for anyone looking to take full control of their smart-home light.

## 8 Walkthrough
[Demo_Video](https://youtu.be/xpGDOYErqfc)
