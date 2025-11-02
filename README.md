# Realtime Face‑Recognition Attendance System  
Developed by Ali Hassan (GitHub: [@Alihassandev1](https://github.com/Alihassandev1))  

## 🚀 Overview  
This project is a real‑time attendance system built using Python, leveraging the `face_recognition` and `opencv‑python` libraries. The aim is to automate attendance tracking by recognising faces from a live video feed and logging attendance to a file or database.

## 🎯 Key Features  
- Real‑time webcam or camera feed processing  
- Face detection and recognition using known face encodings  
- Automatic marking of attendance when a face is recognised  
- Simple setup and minimal configuration  

## 🧭 Why this matters  
Traditional attendance systems (manual roll‑calls, sign‑in sheets) are time‑consuming, error‑prone and can be manipulated. Using face recognition enables a contactless, efficient, and accurate method—ideal for classrooms, offices or workshops.

## 📁 Project Structure (example)  
```
/Realtime‑Face‑Recognition‑Attendance‑System  
│  
├── known_faces/              ← Folder of images of registered persons  
├── encodings.pickle          ← Serialized face encodings of known faces  
├── attendance_log.csv        ← Log file of attendance records  
├── recognize.py              ← Main script for running recognition & logging  
├── train.py                  ← Script to register new persons and generate encodings  
├── requirements.txt          ← Python dependencies  
└── README.md                 ← This document  
```

## 🛠️ Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Alihassandev1/Realtime‑Face‑Recognition‑Attendance‑System‑
   ```  
2. Create and activate a Python virtual environment (recommended).  
3. Install the required dependencies:  
   ```bash
   pip install ‑r requirements.txt
   ```  
4. Populate the `known_faces/` folder with one image of each person you want to track.  
5. Run the `train.py` script to generate face encodings:  
   ```bash
   python train.py
   ```  
6. Start the recognition system:  
   ```bash
   python recognize.py
   ```  
   The script will access your webcam, detect and identify faces, and log attendance accordingly.

## ✅ Usage Notes  
- Ensure adequate lighting and clear visibility of faces for better recognition accuracy.  
- Use a consistent background if possible to improve detection robustness.  
- Update `attendance_log.csv` or adapt the script if you want a different storage (e.g., database).  
- You may want to adjust recognition thresholds (e.g., match tolerance) in the code to balance accuracy vs false‑positives.

## 🔧 Dependencies  
- Python (3.12+ recommended)  
- OpenCV (`opencv‑python`)  
- `face_recognition` library (built on `dlib`)  
- Other standard libraries as listed in `requirements.txt`

## 🧪 How It Works (Simplified)  
1. Load known face images → compute and store their encodings.  
2. Start video capture from camera.  
3. For each video frame:  
   - Detect faces.  
   - Compute encoding for each detected face.  
   - Compare against stored encodings to find matches.  
   - If match found: mark the person as present and log timestamp.  
4. Optionally, display the video feed with bounding boxes and names.

## 📌 Customisation Ideas  
- Integrate with a database (SQLite, MySQL, or PostgreSQL) instead of CSV.  
- Build a GUI (e.g., with Tkinter, PyQt, or a web frontend) for registration and reports.  
- Add multi‑camera support or network camera feeds.  
- Expand to include features like “face not registered” alerts, daily/weekly report generation, or mobile integration.  
- Improve recognition robustness (angles, low light, occlusions) by adding more images or using advanced models.

## 📄 License  
This project is provided as‑is under the MIT License (or your preferred license). Feel free to reuse, modify, and expand the system, with attribution.

## 💡 Acknowledgements  
- The [face_recognition](https://github.com/ageitgey/face_recognition) library by Adam Geitgey for simplifying face recognition in Python.  
- OpenCV for providing fast real‑time image and video processing.

---

*Thank you for checking out the project — and best of luck automating your attendance workflow!*  
