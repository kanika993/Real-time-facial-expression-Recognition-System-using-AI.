
# 🎭 Real-Time Facial Expression Recognition System

An AI-powered real-time facial expression recognition system built using *Python, **OpenCV, and a **Convolutional Neural Network (CNN). This system detects human faces from a live webcam feed and classifies their expressions into categories like **Happy, **Sad, **Angry, **Neutral, and **Surprise* in real time.

---

## 📌 How It Works

1. Open the project folder.
2. Locate the First.py file.
3. *Right-click* on First.py and choose *Run 'First'*.
4. A login window will appear:
   - *User ID:* admin1234
   - *Password:* Admin
5. Click the *Submit* button.
6. The webcam will open and start detecting faces.
7. Detected faces will be recognized, and their expressions will be displayed live on the video stream.
8. **To stop the program, press the Q key** — it will close the webcam window and safely exit the program.

## 📂 Project Structure

Real-time facial expression Recognition System/
│
├── img/                            # Sample images
│   ├── 1.jpg
│   ├── 12.png
│   ├── 101.png
│   └── 319461.png
│
├── model/                          # Trained model files
│   ├── emotion_model.h5
│   └── emotion_model.json
│
├── haarcascade_frontalface_default.xml  # OpenCV face detection config
├── First.py                        # Main application script
├── emodec.py                       # Additional utility (if used)
├── hdd.png                         # Image asset
└── README.md                       # Project documentation

## 📌 Technologies Used

- *Python 3.10*
- *OpenCV*
- *TensorFlow / Keras*
- *Haarcascade Classifier*
- *Convolutional Neural Networks (CNN)*

---

## 📌 Features

- Real-time face detection using Haarcascade.
- Emotion classification into multiple categories.
- Displays emotion labels live on webcam feed.
- Secure login page before starting the recognition.
- Press *Q* to stop the webcam and exit the program.

## 📌 How to Install Dependencies

Open your terminal or Git Bash in the project directory and run:

pip install opencv-python tensorflow keras

---

## 📌 Author

*Kanika Agrawal*

---

## 📌 License

This project is open-source and available for educational and learning purposes.
