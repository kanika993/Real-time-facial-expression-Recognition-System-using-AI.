import cv2
import os
import numpy as np
import random
import webbrowser
import time
import tensorflow as tf
from tensorflow.keras.models import model_from_json, Sequential


with open('model/emotion_model.json', 'r') as json_file:
    loaded_model_json = json_file.read()


emotion_model = model_from_json(loaded_model_json, custom_objects={"Sequential": Sequential})


emotion_model.load_weights("model/emotion_model.h5")
print("✅ Model loaded from disk")


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

emotion_labels = ['Angry', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']


cap = cv2.VideoCapture(0)
ct = 0
current_directory = os.getcwd()


while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]
        face_roi = cv2.resize(face_roi, (48, 48), interpolation=cv2.INTER_AREA)
        face_roi = np.expand_dims(face_roi, axis=0)
        face_roi = np.expand_dims(face_roi, axis=-1)

        predicted_emotion = 'Neutral'
        emotion_probabilities = emotion_model.predict(face_roi)[0]
        max_emotion_index = np.argmax(emotion_probabilities)

        if max_emotion_index < len(emotion_labels):
            predicted_emotion = emotion_labels[max_emotion_index]


        time.sleep(1)
        ct += 1


        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"Emotion: {predicted_emotion}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


    cv2.imshow('-Emotion-', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
