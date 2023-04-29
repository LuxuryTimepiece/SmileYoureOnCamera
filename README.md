# Face Detection with Smiley Faces

This is a Python script that uses OpenCV to perform face detection in real-time using a webcam. It then overlays a smiley face on each detected face.

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
5. To quit the script, press the 'q' key.

## Credits

This code is based on the OpenCV tutorial on [Face Detection using Haar Cascades](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html) and modified to add smiley faces on the detected faces.

## License

This code is licensed under the [MIT License](LICENSE).
