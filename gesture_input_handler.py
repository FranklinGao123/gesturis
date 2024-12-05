import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2
import time

model_path = 'gesture_recognizer.task'

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    # Check if the result is not None before printing
    if result is not None:
        # Store results
        gestureName = []
        handName = []
        for gesture in result.gestures:
            gestureName = [category.category_name for category in gesture for g in result.gestures if g]
        for hand in result.handedness:
            handName = [category.category_name for category in hand for h in result.handedness if h]
        return gestureName
        # print('gesture recognition result: {}'.format(gestureName))
        # print('hand recognition result: {}'.format(handName))
    else:

        # If no gesture is recognized, print a default message
        cv2.putText(output_image, 'No gesture recognized', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.GestureRecognizerOptions(base_options=base_options,running_mode=VisionRunningMode.LIVE_STREAM,result_callback=print_result)
recognizer = vision.GestureRecognizer.create_from_options(options)
# with GestureRecognizer.create_from_options(options) as recognizer:
    # The detector is initialized. Use it here.
    
frame_timestamp_ms = int(round(time.time() * 1000))

# Open the default camera
cam = cv2.VideoCapture(0)

timestamp = 0

# Get the default frame width and height
# frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'mp4v')
# out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

with GestureRecognizer.create_from_options(options) as recognizer:
    while cam.isOpened(): 
        ret, frame = cam.read()

        if not ret:
            print("Ignoring empty frame")
            break
        
        # Write the frame to the output file
        # out.write(frame)

        # Display the captured frame
        cv2.imshow('Camera', frame)
        timestamp += 1
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        
        recognizer.recognize_async(mp_image, timestamp)

        # Press 'q' to exit the loop
        if cv2.waitKey(1) == ord('q'):
            break

# Release the capture and writer objects
cam.release()
# out.release()
cv2.destroyAllWindows()

