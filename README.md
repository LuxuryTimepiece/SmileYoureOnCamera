# Face Detection with OpenCV and Adding Overlaying Smiley Faces

This Python script uses OpenCV to perform real-time face detection using a webcam and overlays a smiley face on each detected face. The number of detected faces is displayed in the upper right corner of the window, and the coordinates of the detected faces are printed in the terminal window.

### How it works

The program loads a pre-trained Haar Cascade classifier for detecting faces from the OpenCV library. It also loads a smiley face image that will be placed over the detected faces.

Then, the program starts capturing frames from the webcam and converts each frame to grayscale. The Haar Cascade classifier is then applied to the grayscale image to detect any faces present in the frame.

If a face is detected, the program scales the smiley face image to match the size of the detected face, creates a mask for the smiley face, and applies it to the image. The program also displays the resulting frame in a window.

Finally, the program prints the coordinates of the detected faces in the terminal window.

## Requirements

- Python 3.x
- OpenCV
- `haarcascade_frontalface_default.xml` file
- `proxy-image.png` file

## Usage

1. Clone this repository to your local machine.
2. Edit the pathway to `haarcascade_frontalface_default.xml` on line 9 and `proxy-image.png` on line 12.
3. Run the script using `python3 SmileYoureOnCamera.py`.
4. The webcam feed will open, and the script will start detecting faces and overlaying smiley faces on them.
5. The number of detected faces is displayed in the upper right corner of the window.
6. The coordinates of the detected faces are printed in the terminal window.
7. To quit the script, press the 'q' key or control C.

## Credits

This code is based on the OpenCV tutorial on [Face Detection using Haar Cascades](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) and modified to add smiley faces on the detected faces.

## License

This code is licensed under the [MIT License](LICENSE).

This program is for educational purposes only and can be modified to suit your specific needs.
