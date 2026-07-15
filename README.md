# facial-emotion-recognition
# 😊 Facial Emotion Recognition

A real-time Facial Emotion Recognition system built using **Python, OpenCV, DeepFace, and Streamlit**. The application analyzes facial expressions from uploaded images (or webcam, if supported) and predicts the dominant emotion.

Features

- Detects faces in images
- Recognizes emotions such as:
  - Happy 😊
  - Sad 😢
  - Angry 😠
  - Surprise 😲
  - Fear 😨
  - Disgust 🤢
  - Neutral 😐
- Simple Streamlit web interface
- Easy to deploy on Streamlit Cloud

Technologies Used

- Python
- OpenCV
- DeepFace
- TensorFlow
- Streamlit
- NumPy
- Pandas

Project Structure

```
Facial-Emotion-Recognition/
│── app.py
│── requirements.txt
│── README.md
│── assets/
│── sample_images/
```

Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Facial-Emotion-Recognition.git
cd Facial-Emotion-Recognition
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

Screenshots

Add screenshots of your application here.

Future Improvements

- Live webcam emotion detection
- Emotion history and analytics
- Multiple face detection
- Better UI/UX
- Export results to CSV

License

This project is developed for educational purposes.
