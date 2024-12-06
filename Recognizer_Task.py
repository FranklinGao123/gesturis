import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import cv2

class Recognizer_Task:
    
    def __init__(self):
        self.camera = cv2.VideoCapture(0)
        self.output = self.video_output()
        self.timestamp = 0
        self.ges = []
    
    def video_output(self):
        # Get the default frame width and height
        frame_width = int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
        # Define the codec and create VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))
        return out  
      
    def recognition(self):
        base_options = python.BaseOptions(model_asset_path='gesture_recognizer.task')
        options = vision.GestureRecognizerOptions(base_options=base_options,running_mode=vision.RunningMode.LIVE_STREAM,min_hand_presence_confidence=0.3,min_hand_detection_confidence=0.3,result_callback=self.listener)
        recognizer = vision.GestureRecognizer.create_from_options(options)
        
        # with vision.GestureRecognizer.create_from_options(options) as recognizer:
        # while self.camera.isOpened(): 
        
        ret, frame = self.camera.read()

        if not ret:
            print("Ignoring empty frame")
            return
        
        # Write the frame to the output file
        self.output.write(frame)

        # Display the captured frame
        cv2.imshow('Camera', frame)
        self.timestamp += 1
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
        
        recognizer.recognize_async(mp_image, self.timestamp)
        
        print (self.ges) 
        return self.ges 
    
        
        # Press 'q' to exit the loop
        # if cv2.waitKey(1) == ord('q'):
        #     break


    # Create a gesture recognizer instance with the live stream mode:
    def listener(self, result: vision.GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
        # Check if the result is not None before printing
        if result is not None:
            # Store results
            gestureName = []
            handName = []
            for gesture in result.gestures:
                gestureName = [category.category_name for category in gesture for g in result.gestures if g]
            for hand in result.handedness:
                handName = [category.category_name for category in hand for h in result.handedness if h]
            print('gesture recognition result: {}'.format(gestureName))
            print('hand recognition result: {}'.format(handName))
            self.ges = gestureName
            print (self.ges)
        else:
        # If no gesture is recognized, print a default message
            cv2.putText(output_image, 'No gesture recognized', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    # Release the capture and writer objects
    def kill_cam(self):
        self.camera.release()
        self.output.release()
        cv2.destroyAllWindows()
    
    