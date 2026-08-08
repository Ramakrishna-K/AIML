from camera.webcam import Webcam
from camera.mobile_camera import MobileCamera


class CameraStream:

    def __init__(
        self,
        source="webcam",
        camera_index=0,
        mobile_url=None
    ):

        if source == "webcam":
            self.camera = Webcam(camera_index)

        elif source == "mobile":

            if mobile_url is None:
                raise ValueError("mobile_url is required.")

            self.camera = MobileCamera(mobile_url)

        else:
            raise ValueError("Invalid camera source.")

    def read(self):
        return self.camera.read()

    def release(self):
        self.camera.release()