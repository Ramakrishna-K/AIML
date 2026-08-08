import cv2


class FaceDrawer:

    @staticmethod
    def draw_face(frame, location, name="Unknown"):

        top, right, bottom, left = location

        # Face Rectangle
        cv2.rectangle(
            frame,
            (left, top),
            (right, bottom),
            (0, 255, 0),
            2
        )

        # Name Background
        cv2.rectangle(
            frame,
            (left, bottom - 30),
            (right, bottom),
            (0, 255, 0),
            cv2.FILLED
        )

        # Name
        cv2.putText(
            frame,
            name,
            (left + 5, bottom - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (255, 255, 255),
            2
        )

    @staticmethod
    def draw_fps(frame, fps):

        cv2.putText(
            frame,
            f"FPS: {fps:.2f}",
            (20, 35),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 255),
            2
        )