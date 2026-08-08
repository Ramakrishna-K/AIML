import cv2


class Webcam:

    def __init__(self, camera_index=0):
        self.cap = cv2.VideoCapture(camera_index)

        if not self.cap.isOpened():
            raise Exception("Cannot open webcam.")

    def read(self):
        success, frame = self.cap.read()
        return success, frame

    def release(self):
        self.cap.release()