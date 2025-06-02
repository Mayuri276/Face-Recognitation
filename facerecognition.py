import cv2
import face_recognition
#Load know face encodings and names
known_face_encodings = []
known_face_names = []
#Load knows faces and their names here
known_person1_image = face_recognition.load_image_file(r"C:\Users\Mayuri Jamdar\Desktop\offices\who is he\photo\Mayuri Jamdar .jpeg")
known_person2_image = face_recognition.load_image_file(r"C:\Users\Mayuri Jamdar\Desktop\offices\who is he\photo\Darshan Raval.jpg")
known_person3_image = face_recognition.load_image_file(r"C:\Users\Mayuri Jamdar\Desktop\offices\who is he\photo\Sharukh khan.jpg")
known_person4_image = face_recognition.load_image_file(r"C:\Users\Mayuri Jamdar\Desktop\offices\who is he\photo\Vaishnavi.jpeg")
known_person5_image = face_recognition.load_image_file(r"C:\Users\Mayuri Jamdar\Desktop\offices\who is he\photo\Kanchan.jpeg")

known_person1_encoding = face_recognition.face_encodings(known_person1_image)[0]
known_person2_encoding = face_recognition.face_encodings(known_person2_image)[0]
known_person3_encoding = face_recognition.face_encodings(known_person3_image)[0]
known_person4_encoding = face_recognition.face_encodings(known_person4_image)[0]
known_person5_encoding = face_recognition.face_encodings(known_person5_image)[0]
known_face_encodings.append(known_person1_encoding)
known_face_encodings.append(known_person2_encoding)
known_face_encodings.append(known_person3_encoding)
known_face_encodings.append(known_person4_encoding)
known_face_encodings.append(known_person5_encoding)

known_face_names.append("Mayuri Jamdar")
known_face_names.append("Darshan Raval")
known_face_names.append("Sharukh Khan")
known_face_names.append("Vaishnavi")
known_face_names.append("Kanchan")

#Initialize webcam
Video_capture = cv2.VideoCapture(0)  
while True :
    # Capture frame-by-frame
    ret , frame = Video_capture.read()

    #Final all face locations in the current frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    #Loop through each face found in the frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        #check if the face matches any known faces
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Unknown"

        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        #Draw a box around the face and label with the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,0,255), 2)

    #Display the resulting frame
    cv2.imshow("Video", frame)

    #Break the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the webcam and close opencv windows
Video_capture.release()
cv2.destroyAllWindows()
