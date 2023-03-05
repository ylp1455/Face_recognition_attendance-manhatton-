import face_recognition
import cv2
import numpy as np
import os
import csv
from datetime import datetime

video_capture = cv2.VideoCapture(0)

sachin_image = face_recognition.load_image_file('images/sachin.jpg')
sachin_encoding = face_recognition.face_encodings(sachin_image)[0]

lakshan_image = face_recognition.load_image_file('img/lakshan.jpg')
lakshan_encoding = face_recognition.face_encodings(lakshan_image)[0]

dunnamkannam_image = face_recognition.load_image_file('img/dunnamkann.jpg')
dunnamkannam_encoding = face_recognition.face_encodings(dunnamkannam_image)[0]

known_face_encodings = [
    sachin_encoding,
    lakshan_encoding,
    dunnamkannam_encoding
]

known_face_names = [
    'Sachin',
    'Lakshan',
    'Dunnamkannam'
]

students = known_face_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

now = datetime.now()
current_date = now.strftime("%Y-%m-%d")

f = open(current_date + ".csv", "w+", newline='')
lnwriter = csv.writer(f)

while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]

    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = ""

            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

            face_names.append(name)
            if name in known_face_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    lnwriter.writerow([name, current_time])

        cv2.imshow("attendance system", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video_capture.release()
cv2.destroyAllWindows()
f.close()
