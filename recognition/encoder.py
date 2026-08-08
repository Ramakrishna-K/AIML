
from insightface.app import FaceAnalysis


class FaceEncoder:

    def __init__(self):

        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640)
        )

    def encode(self, frame):
        """
        Detect faces and generate embeddings.
        """

        faces = self.app.get(frame)

        embeddings = []

        boxes = []

        for face in faces:

            embeddings.append(face.embedding)

            boxes.append(
                face.bbox.astype(int)
            )

        return embeddings, boxes