# User will need to edit pathway to haarcascade_frontalface_default.xml on line 9 and the proxy-image.png on line 12

import cv2
import os
import subprocess

def main():
    # Load the cascade classifier
    face_cascade = cv2.CascadeClassifier("/path/to/the/file/haarcascade_frontalface_default.xml")

    if face_cascade.empty():
        print("Error: Cascade file not found.")
        return

    # Load the smiley face image
    smiley_face = cv2.imread("/path/to/the/file/proxy-image.png", -1)

    if smiley_face is None:
        print("Error: Smiley face image not found.")
        return

    # Start the webcam
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

        for (x, y, w, h) in faces:
            smiley_face_resized = cv2.resize(smiley_face, (w, h), interpolation=cv2.INTER_CUBIC)
            mask = smiley_face_resized[:, :, 2]
            mask_inv = cv2.bitwise_not(mask)
            roi = frame[y:y + h, x:x + w]

            roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
            roi_fg = cv2.bitwise_and(smiley_face_resized, smiley_face_resized, mask=mask)
            dst = cv2.add(roi_bg, roi_fg)
            frame[y:y + h, x:x + w] = dst

            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, f"Faces detected: {len(faces)}", (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Print the coordinates of detected faces
    print(f"Detected faces: {faces}")

if __name__ == "__main__":
    main()
