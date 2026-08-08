import cv2


class MobileCamera:

    def __init__(self, url):
        self.cap = cv2.VideoCapture(url)

        if not self.cap.isOpened():
            raise Exception("Cannot connect to mobile camera.")

    def read(self):
        success, frame = self.cap.read()
        return success, frame

    def release(self):
        self.cap.release()