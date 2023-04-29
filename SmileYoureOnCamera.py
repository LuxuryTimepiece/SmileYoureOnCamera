# user may need to edit pathway to haarcascade_frontalface_default.xml on line 9 and the proxy-image.png on line 12

import cv2
import numpy as np
import os
import subprocess

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier("/path/to/the/file/haarcascade_frontalface_default.xml")

# Load the smiley face image
smiley_face = cv2.imread("/path/to/the/file/proxy-image.png", -1)

# Start the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read the frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=5)

    # Draw smiley faces around the faces
    for (x, y, w, h) in faces:
        smiley_face_resized = cv2.resize(smiley_face, (w, h),
                                        interpolation=cv2.INTER_CUBIC)

        # Create a mask for the smiley face
        # mask = smiley_face_resized[:, :, 3] <-- looking for alpha channel
        mask = smiley_face_resized[:, :, 2]
        mask_inv = cv2.bitwise_not(mask)
        roi = frame[y:y + h, x:x + w]

        # Black out the area behind the smiley face
        roi_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        # Take only region of smiley face from smiley_face_resized image
        roi_fg = cv2.bitwise_and(smiley_face_resized, smiley_face_resized, mask=mask)

        # Put smiley_face_resized in ROI
        dst = cv2.add(roi_bg, roi_fg)
        frame[y:y + h, x:x + w] = dst


        # Display the number of faces detected on the "Face Detection" window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Faces detected: " + str(len(faces)), (10, 30), font, 1, (255, 255, 255), 2, cv2.LINE_AA)

    # Display the resulting frame in a window
    cv2.imshow("Face Detection", frame)

    # Open a new terminal window and print the contents of face_cascade
    os.system("open -a Terminal.app")
    subprocess.run(["echo", str(faces)], check=True, text=True)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
