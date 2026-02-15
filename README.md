# 🎙️ Tkinter VU Meter with Shout Detection

A simple real-time VU (Volume Unit) meter built with Tkinter that monitors microphone input, converts sound levels to decibels, and warns the user when they are shouting using a color-changing visual bar.

---

## 🚀 Features

* 🎧 Real-time microphone input monitoring
* 📊 Live VU meter with smooth animation
* 🎨 Color-coded intensity levels

  * 🟢 Green → Normal voice
  * 🟡 Yellow → Loud voice
  * 🔴 Red → Shouting
* ⚠️ Displays **"STOP SHOUTING"** warning when threshold is exceeded
* 🧠 RMS-based decibel calculation
* ✨ Smooth UI updates using Tkinter

---

## 🛠️ Technologies Used

* Python
* Tkinter (GUI)
* NumPy (Audio Processing)
* SoundDevice (Microphone Input)
* Math Module

---

## 📂 Project Structure

```
vu-meter/
│
├── vuMeter.py
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/vu-meter.git
cd vu-meter
```

### 2️⃣ Install Required Dependencies

```
pip install sounddevice numpy
```

> Tkinter is included with most Python installations.

---

## ▶️ How to Run

```
python vuMeter.py
```

Make sure:

* Your microphone is connected
* The correct input device index is set (currently `device=1` in the code)

To check available input devices:

```python
import sounddevice as sd
print(sd.query_devices())
```

---

## 📐 How It Works

### 🎵 Audio Processing

* Captures microphone input using `sounddevice`
* Calculates RMS (Root Mean Square) value
* Converts RMS to decibels:

```
dB = 20 * log10(rms)
```

* Applies smoothing to prevent sudden jumps in the meter

---

### 🎨 Visual Representation

The VU bar changes color based on the decibel level:

| dB Range      | Color  | Meaning      |
| ------------- | ------ | ------------ |
| < -30 dB      | Green  | Normal voice |
| -30 to -10 dB | Yellow | Loud voice   |
| > -10 dB      | Red    | Shouting     |

---

## ⚠️ Warning System

When volume exceeds the defined threshold:

```
SHOUT_DB = -10
```

The program:

* Turns the bar red
* Displays "STOP SHOUTING"
* Uses cooldown logic to prevent repeated warnings

---

## 🧪 Customization

You can modify these values in the code:

```
MAX_DB = 60
SHOUT_DB = -10
WARNING_COOLDOWN = 2
```

* Adjust sensitivity
* Change shout detection threshold
* Modify warning delay

---

## 🎯 Learning Outcomes

* Real-time audio signal processing
* RMS to decibel conversion
* Tkinter GUI development
* Callback-based streaming
* Smoothing algorithms

---

## 👨‍💻 Author

**ADITYA BHARDWAJ**
Section: D2
Roll No: 08
Course: B.Tech
Branch: CSE

---

## 📌 Future Improvements

* Add waveform visualization
* Add peak hold indicator
* Add adjustable threshold slider
* Add sound logging feature
* Package into executable (.exe)

---

This project demonstrates practical implementation of real-time audio monitoring with graphical feedback using Python.
