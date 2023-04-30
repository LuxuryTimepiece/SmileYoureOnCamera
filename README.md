# Face Detection with Smiley Faces

This is a Python script that uses OpenCV to perform face detection in real-time using a webcam. It then overlays a smiley face on each detected face. When faces are detected, script will print number of faces detected in upper right of window. Lastly, in terminal window, the script is continually printing the coordinates of any detected faces.

## Requirements

- Python 3.x
- OpenCV
- `haarcascade_frontalface_default.xml` file
- `proxy-image.png` file

## Usage

1. Clone this repository to your local machine.
2. Edit the pathway to `haarcascade_frontalface_default.xml` on line 9 and the `proxy-image.png` on line 12.
3. Run the script.

```bash
python3 SmileYoureOnCamera.py
```

4. The webcam will open, and the script will begin detecting faces and overlaying smiley faces on them.
5. When faces are detected, script will print number of faces detected in upper right of window.
5. Script will prints the coordinates of the detected faces in terminal window.
6. To quit the script, press the 'q' key or control C

## Credits

This code is based on the OpenCV tutorial on [Face Detection using Haar Cascades](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) and modified to add smiley faces on the detected faces.

## License

This code is licensed under the [MIT License](LICENSE).



## Face Detection with OpenCV

This is a Python program that uses OpenCV library to detect faces in real time using a webcam. It draws smiley faces around the detected faces, displays the number of faces detected, and prints the coordinates of the faces in a new terminal window.

### How it works

The program loads a pre-trained Haar Cascade classifier for detecting faces from the OpenCV library. It also loads a smiley face image that will be used to draw around the detected faces.

Then, the program starts capturing frames from the webcam and converts each frame to grayscale. The Haar Cascade classifier is then applied to the grayscale image to detect any faces present in the frame.

If a face is detected, the program resizes the smiley face image to match the size of the detected face, creates a mask for the smiley face, and applies it to the image. Finally, the program displays the resulting frame in a window.

The program also opens a new terminal window and prints the coordinates of the detected faces.

### How to use it

To use this program, follow these steps:

1. Clone the repository or download the `SmileYoureOnCamera` files.
2. Edit the pathway to the `haarcascade_frontalface_default.xml` file and the `proxy-image.png` file if necessary, on lines 9 and 12 respectively.
3. Open a terminal window and navigate to the directory where the `SmileYoureOnCamera.py` file is located.
4. Run the command `python3 SmileYoureOnCamera.py` to start the program.
5. A window will open showing the real-time feed from the webcam with smiley faces drawn around detected faces. The number of detected faces will be displayed in the window.
6. A new terminal window will also open displaying the coordinates of the detected faces.

### Additional notes

To exit the program, press the 'q' key on your keyboard.

This program is for educational purposes only and can be modified to suit your specific needs.
