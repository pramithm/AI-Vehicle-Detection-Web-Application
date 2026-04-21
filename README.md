# 🚗 AI Vehicle & Human Detection Web Application

## 📌 Overview

This project is a real-time **AI-powered web application** that detects and classifies objects from a live camera feed or video input.
The system identifies and categorizes objects into:

* 🧍 Human
* 🏍️ 2-Wheeler
* 🚗 4-Wheeler
* 🚛 6-Wheeler

It uses deep learning-based object detection to provide accurate and real-time results.

---

## 🎯 Features

* Real-time object detection using webcam
* Classification into vehicle categories and humans
* Bounding box visualization with labels
* Scalable web application using Flask
* Clean and modular project structure

---

## 🧠 Technologies Used

* Python
* Flask (Backend)
* OpenCV (Computer Vision)
* YOLOv8 (Object Detection Model)
* HTML, CSS, JavaScript (Frontend)

---

## 🏗️ Project Structure

```
vehicle-detection-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── model/
│   └── detector.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── uploads/
│
├── templates/
│   └── index.html
│
├── utils/
│
└── venv/ (ignored)
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/AI-Vehicle-Detection-Web-Application.git
cd AI-Vehicle-Detection-Web-Application
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate   # Windows
```

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Run Detection (Standalone)

```
python model/detector.py
```

### Run Web App

```
python app.py
```

Then open in browser:

```
http://127.0.0.1:5000/
```

---

## 🧩 How It Works

1. Camera captures live video frames
2. YOLO model processes each frame
3. Objects are detected and classified
4. Results are displayed with bounding boxes
5. Flask streams output to the web interface

---

## 📸 Output

> Added screenshots of:

* Detection output
* Web interface
* Project demo

---

## 🚀 Future Enhancements

* Vehicle counting system
* Speed estimation
* Dashboard with analytics
* Database integration
* Cloud deployment

---

## ⚠️ Notes

* `venv/` is not included in the repository
* Model file (`yolov8n.pt`) will be downloaded automatically
* Requires Python 3.8+

---

## 👨‍💻 Author

**Pramith Maredukonda**
AI Engineer | Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a star on GitHub ⭐
