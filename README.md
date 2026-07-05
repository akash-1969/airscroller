# 🖐️ AirScroller

Control scrolling using hand gestures and a webcam.

AirScroller uses Computer Vision to detect hand gestures in real-time and converts them into scrolling actions, enabling touchless interaction with your computer.

---

## 🚀 Features

- Real-time hand tracking using MediaPipe
- Webcam-based gesture recognition
- Index finger movement controls scrolling
- Open palm gesture toggles scroll direction
- Supports both upward and downward scrolling
- Lightweight and low latency

---

## 🛠️ Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

---

## 🎮 Gesture Controls

| Gesture | Action |
|----------|--------|
| ✋ Open Palm | Toggle between UP and DOWN scrolling mode |
| ☝️ Move Index Finger | Scroll in the currently selected direction |
| ☝️ Faster Finger Movement | Faster scrolling |
| ☝️ Slower Finger Movement | Slower scrolling |

---

## ⚙️ How It Works

1. OpenCV captures frames from the webcam.
2. MediaPipe detects hand landmarks in real-time.
3. An open palm gesture toggles the scrolling direction.
4. Index finger movement determines scroll intensity.
5. PyAutoGUI sends mouse wheel events to the operating system.

---

## 📂 Project Structure

```text
airscroller/
├── .gitignore
├── main.py
└── test.py
```

### File Description

- `main.py` → Main AirScroller application.
- `test.py` → Gesture experiments and testing.
- `.gitignore` → Prevents unnecessary files from being pushed to GitHub.
- `venv/` and `venv312/` → Local Python virtual environments.

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/airscroller.git
cd airscroller
```

Install dependencies:

```bash
pip install opencv-python mediapipe pyautogui
```

Run the application:

```bash
python main.py
```

---

## 🧠 MediaPipe Landmarks Used

| Landmark | Purpose |
|----------|---------|
| 8 | Index fingertip for scrolling |
| 12 | Middle fingertip for palm detection |
| 16 | Ring fingertip for palm detection |
| 20 | Pinky fingertip for palm detection |

---

## 🔮 Future Improvements

- Mouse cursor control
- Volume control gestures
- Brightness control gestures
- Custom gesture mapping
- Multi-hand support

---

## 📄 License

This project is open source and available under the MIT License.

---

## ⭐ Star the repository if you found it interesting!
