from djitellopy import Tello
import time
#import cv2

tello = Tello()

tello.connect()
print('connect')

# Create OpenCV window
cv2.namedWindow("Tello Video Stream", cv2.WINDOW_NORMAL)

# Takeoff
tello.takeoff()
print('takeoff')
time.sleep(1)
tello.move_forward(140)
print('forward 1')
time.sleep(2)  # Allow time for takeoff

# Main loop for video display and object detection
try:
    while True:
        # Read frame from video stream
        frame = tello.get_frame_read().frame

        # Object detection using YOLO
        _, labels, _ = cv.detect_common_objects(frame)
        tello.move_forward(140)
        time.sleep(1)

        # If 'person' is detected, move backward
        if 'person' in labels:
            tello.move_back(30)  # Adjust the speed as needed
        else:
            tello.move_forward(30)  # Adjust the speed as needed

        # Display the frame with bounding boxes
        frame = cv.object_detection.draw_bbox(frame, cv.get_objects(frame, labels))
        cv2.imshow("Tello Video Stream", frame)
        tello.rotate_clockwise(90)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

finally:
    # Land and stop video stream
    tello.land()
    tello.streamoff()
    cv2.destroyAllWindows()

tello.land()