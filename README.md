# 🖐️ Hand Gesture Web Controller

Control your web browser using real-time hand gestures powered by Computer Vision.

This project uses **OpenCV**, **MediaPipe**, **PyAutoGUI**, and **Tkinter** to detect hand gestures through a webcam and perform browser operations such as mouse movement, scrolling, clicking, and tab management.

---

## 🚀 Features

- 🎯 Real-time hand tracking using MediaPipe
- 🖱️ Control mouse pointer using index finger
- 👌 Click using thumb-index pinch gesture
- 📜 Scroll pages using two-finger gesture
- ➕ Open new browser tab
- ⬅️ Switch to previous tab
- ➡️ Switch to next tab
- 🖥️ Simple Tkinter GUI to Start/Stop Gesture Control
- 🧩 Modular and scalable project architecture

---

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- Tkinter
- NumPy

---

# Gesture Mapping

| Gesture | Action |
|---------|--------|
| ☝️ Index Finger | Move Mouse Cursor |
| 👌 Thumb + Index | Left Click |
| ✌️ Two Fingers | Scroll |
| 🤙 Thumb + Pinky | Open New Tab |
| 🤞 Three Fingers | Previous Tab |
| 🖖 Four Fingers | Next Tab |

---

# Project Structure

```text
HAND_GESTURE_WEBCONTROL/
│
├── assets/
├── build/
├── dist/
│   └── main.exe
│
├── models/
│
├── venv/
│
├── browser_controller.py
├── camera.py
├── config.py
├── gesture_classifier.py
├── gesture_ui.py
├── hand_gesture.py
├── main.py
├── utils.py
│
├── requirements.txt
├── Gesture_Controller.bat
├── main.spec
├── .gitignore
└── README.md
```

---

# Project Architecture

```text
 Webcam
    │
    ▼
Camera Module
    │
    ▼
Hand Detection
(MediaPipe)
    │
    ▼
Gesture Classifier
    │
    ▼
Browser Controller
(PyAutoGUI)
    │
    ▼
Browser Actions
```

---

# Modules

### 📷 camera.py

- Opens webcam
- Captures frames
- Returns frames to the application

---

### ✋ hand_gesture.py

- Detects hand landmarks
- Uses MediaPipe Hands
- Returns detected landmarks

---

### 🧠 gesture_classifier.py

Responsible for recognizing gestures using landmark positions.

Examples:

- Index Finger
- Pinch
- Two Fingers
- Three Fingers
- Four Fingers
- Thumb + Pinky

---

### 🌐 browser_controller.py

Maps gestures to browser operations.

Examples:

- Mouse Movement
- Left Click
- Scroll
- Next Tab
- Previous Tab
- New Tab

---

### 🖥️ gesture_ui.py

Tkinter-based graphical interface.

Features:

- Start Gesture Controller
- Stop Gesture Controller

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Hand-Gesture-WebController.git
```

Move into the project

```bash
cd Hand-Gesture-WebController
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python main.py
```

---

# Build Executable

```bash
pyinstaller main.spec
```

Executable will be generated inside

```text
dist/
```

---

# Future Improvements

- Gesture smoothing
- Gesture confidence filtering
- Custom gesture recording
- Hugging Face gesture recognition model
- AI-based gesture classification
- Voice + Gesture control
- Multi-monitor support

---

# Learning Outcomes

This project helped in understanding:

- Computer Vision fundamentals
- MediaPipe Hands
- Human Computer Interaction (HCI)
- Real-time image processing
- Python GUI development
- Modular software architecture
- Browser automation

---

# Author

**Aryan Baakle**

Artificial Intelligence & Data Science Student

Passionate about AI, Computer Vision and Generative AI.

---

## ⭐ If you found this project interesting, consider giving it a star!
