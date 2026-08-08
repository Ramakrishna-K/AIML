import cv2


class FaceAligner:

    def __init__(self):
        pass

    def align(self, frame, face_location):
        """
        Crop the detected face.

        Returns:
            aligned_face
        """

        top, right, bottom, left = face_location

        face = frame[top:bottom, left:right]

        if face.size == 0:
            return None

        aligned = cv2.resize(
            face,
            (160, 160)
        )

        return aligned