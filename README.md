
# FaceMark: AI-Powered Attendance System


## Overview

**FaceMark** is an innovative attendance system that leverages AI-driven facial recognition to automate and streamline the process of marking attendance. By recognizing faces through a camera, FaceMark offers a seamless, efficient, and secure method of tracking attendance, making it an ideal solution for educational institutions, workplaces, and events.

## Features

- **Real-Time Facial Recognition**: Automatically detects and records attendance by recognizing faces in real time.
- **High Accuracy**: Utilizes advanced AI algorithms to ensure precise and reliable attendance marking.
- **User-Friendly Interface**: Simple and intuitive design for easy setup and use.
- **Secure Data Handling**: Safeguards personal data with encryption and secure storage.
- **Customizable Settings**: Configure recognition parameters to meet specific requirements.

## Installation

### Prerequisites

- Python 3.7+
- OpenCV
- dlib
- face_recognition library

### Clone the Repository

```bash
git clone https://github.com/atharv2001j/FaceMark-AI-Powered-Attendance-System.git
cd FaceMark-AI-Powered-Attendance-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Configuration

1. **Setup**: Place images of the individuals in the `known_faces` directory. Each image should be named after the individual (e.g., `atharv.jpg`).

2. **Run the System**: Execute the main script to start the attendance system.

```bash
python app.py
```

## Usage

1. **Start Camera**: The system will access the camera and begin scanning for faces.
2. **Mark Attendance**: Detected faces are cross-referenced with the known faces database, and attendance is automatically recorded.
3. **View Attendance Records**: Attendance logs are stored in a CSV file for easy access and analysis.

## Acknowledgments

- Thanks to the developers of [OpenCV](https://opencv.org/), [dlib](http://dlib.net/), and the [face_recognition](https://github.com/ageitgey/face_recognition) library for their incredible tools.

## Contact

For any inquiries or support, please contact [joshiatharv67@gmail.com](mailto:joshiatharv67@gmail.com).

