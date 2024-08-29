import cv2
import numpy as np
import face_recognition
from datetime import datetime
import csv
import streamlit as st
import pandas as pd

# Initialize the video capture from the default camera (index 0)
cap = cv2.VideoCapture(0)

# Load image file and encode face for each known person
atharv = face_recognition.load_image_file(r'D:\projects\AI Attendance System\data\Images\atharv.png')
atharv_encoded = face_recognition.face_encodings(atharv)[0]

dq = face_recognition.load_image_file(r'D:\projects\AI Attendance System\data\Images\dq.jpg')
dq_encoded = face_recognition.face_encodings(dq)[0]

yash = face_recognition.load_image_file(r'D:\projects\AI Attendance System\data\Images\yash.jpeg')
yash_encoded = face_recognition.face_encodings(yash)[0]

messi = face_recognition.load_image_file(r'D:\projects\AI Attendance System\data\Images\messi.jpg')
messi_encoded = face_recognition.face_encodings(messi)[0]

tejas = face_recognition.load_image_file(r'D:\projects\AI Attendance System\data\Images\tejas.jpeg')
tejas_encoded = face_recognition.face_encodings(tejas)[0]

sanket = face_recognition.load_image_file(r'D:\projects\AI Attendance System\data\Images\sanket.jpeg')
sanket_encoded = face_recognition.face_encodings(sanket)[0]

# List of all known face encodings and corresponding names
known_faces = [atharv_encoded, dq_encoded, yash_encoded, messi_encoded, tejas_encoded, sanket_encoded]
known_faces_names = ['Atharv Joshi', 'Dq', 'Yash Chavan', 'Messi', 'Tejas Dehade', 'Sanket Gadekar']
students=known_faces_names.copy()
# Initialize a CSV file for attendance logging
current_date = datetime.now().strftime('%Y-%m-%d')
csv_filename = current_date + '.csv'
f = open(csv_filename, 'w+', newline='')
writer = csv.writer(f)

# Streamlit web application layout
st.title('Face Recognition Attendance System')

# Display the webcam feed
st.write('### Webcam Feed')
video_feed = st.empty()

# Continuously capture frames and perform face recognition
while True:
    ret, frame = cap.read()
    
    if not ret:
        break

    # Resize the frame to a smaller size (20% of original) for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.2, fy=0.2)

    # Perform face recognition operations
    face_locations = face_recognition.face_locations(small_frame)
    face_encodings = face_recognition.face_encodings(small_frame, face_locations)
    
    face_names = []
    
    for face in face_encodings:
        matches = face_recognition.compare_faces(known_faces, face)
        name = ''
        face_distances = face_recognition.face_distance(known_faces, face)
        best_match_index = np.argmin(face_distances)
        
        if matches[best_match_index]:
            name = known_faces_names[best_match_index]
        
        face_names.append(name)
        
        if name in known_faces_names:
            if name in students:
                students.remove(name)
                print(students)
                st.write(f'Attendance recorded for: {name}')
                writer.writerow([name, current_date])

    # Display the processed video feed with detected faces
    video_feed.image(frame, channels='BGR')

    # Check for 'a' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# Release the video capture object
cap.release()

# Close the CSV file
f.close()

# Display the CSV file content
st.write('### Attendance CSV')
st.write(f'Showing attendance for date: {current_date}')
df = pd.read_csv(csv_filename)
st.dataframe(df)

# Optionally, you can also download the CSV file
st.download_button(
    label="Download CSV",
    data=open(csv_filename, 'rb').read(),
    file_name=csv_filename,
    mime='text/csv'
)