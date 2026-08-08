


import cv2

from insightface.app import FaceAnalysis


class FaceDetector:

    def __init__(self):

        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640)
        )

    def detect(self, frame):
        """
        Detect faces in a BGR frame.

        Returns:
            faces
        """

        faces = self.app.get(frame)

        return faces