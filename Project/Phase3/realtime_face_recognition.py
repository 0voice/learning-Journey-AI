def realtime_face_recognition():
    import cv2
    import face_recognition
    known_image = face_recognition.load_image_file("known.jpg")
    known_encoding = face_recognition.face_encodings(known_image)[0]

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        rgb = frame[:, :, ::-1]
        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)
        for (top, right, bottom, left), encoding in zip(faces, encodings):
            match = face_recognition.compare_faces([known_encoding], encoding)[0]
            name = "Known" if match else "Unknown"
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)
        cv2.imshow("Face Recognition", frame)
        if cv2.waitKey(1) == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
