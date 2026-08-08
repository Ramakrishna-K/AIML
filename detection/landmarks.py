

from insightface.app import FaceAnalysis


class FaceLandmarks:

    def __init__(self):

        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640)
        )

    def get_landmarks(self, frame):
        """
        Returns facial landmarks for each detected face.

        Output:
        [
            {
                "bbox": face.bbox,
                "landmarks": face.kps
            },
            ...
        ]
        """

        faces = self.app.get(frame)

        results = []

        for face in faces:

            results.append(
                {
                    "bbox": face.bbox.astype(int),
                    "landmarks": face.kps.astype(int)
                }
            )

        return results