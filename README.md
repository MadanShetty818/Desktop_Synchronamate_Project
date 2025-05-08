# 🔊 Desktop_Synchronamate – AI-Powered Desktop Voice Assistant

Synchronamate is an intelligent voice-controlled desktop assistant developed in Python. It listens to voice commands and automates tasks on your system, making daily operations hands-free and efficient. Whether you want to play music, fetch weather updates, or perform calculations, Synchronamate responds in real-time with interactive GUI support.

---

## 📽️ Demo & Screenshots

### 🎬 Desktop UI (Tkinter)
<img src="update.png" width="300" height="auto">

---

## 🚀 Key Features

| Category        | Description |
|----------------|-------------|
| 💬 Voice Control | Recognizes spoken commands using Google's Speech Recognition API |
| 📚 Knowledge Base | Answers general knowledge via **Wikipedia** and **WolframAlpha** |
| 🌐 Web Tasks | Opens YouTube, Google, Instagram, WhatsApp Web, Twitter, etc. |
| 🎧 Media Playback | Plays music from a local directory |
| 🧮 Calculator | Performs addition, subtraction, multiplication, division |
| 📷 Screenshot & Camera | Takes screenshots and captures images using webcam |
| 📂 File Explorer | Opens specific folders like C:\, D:\, Downloads, Pictures, Documents |
| 📦 System Operations | Shutdown, restart, sleep, lock system, empty recycle bin |
| ⏰ Date & Time | Reads current time |
| 📝 Notes | Writes and reads notes with optional timestamps |
| 🌤️ Weather Report | Real-time weather using **OpenWeatherMap API** |
| 😂 Jokes | Tells random jokes with the `pyjokes` module |
| 🔈 Volume Control | Increase or decrease system volume programmatically |
| 🧠 Memory | Remembers user-input notes (stored in `data.txt`) |
| 🧑‍💻 Personalized | Recognizes user's name and greets accordingly |
| 🖼️ Graphical UI | User interface built with Tkinter and image background |

---

## 🧰 Tech Stack

- **Python 3.x**
- **SpeechRecognition** – For capturing and converting speech to text
- **pyttsx3** – Text-to-speech engine (offline)
- **wikipedia** – Fetches summarized info
- **wolframalpha** – Computational knowledge engine
- **Tkinter** – GUI window with interactive labels/buttons
- **pyjokes** – For fun interaction
- **pytube** – YouTube video downloader
- **OpenWeatherMap API** – Real-time weather updates
- **pycaw** – Volume control interface
- **pyautogui & ecapture** – Screenshots and webcam access
- **Twilio, smtplib** – Email/SMS (optional)

---

## 📂 Project Directory Structure
### synchronamate/
### ├── data.txt # Stores remembered user notes
### ├── img.jpg # Captured image via webcam (ecapture)
### ├── update.png # Assistant command output screenshot
### ├── window.png # Background image for the GUI
### └── README.md # Project documentation (this file)

## 📥 Download the Project

📦 <a href="https://github.com/MadanShetty818/Desktop_Synchronamate_Project/blob/main/Desktop_Synchronamate.zip" download>Click here to download Synchronamate (ZIP)</a>

