

import os
import cv2

from insightface.app import FaceAnalysis


class FaceDatabase:

    def __init__(self, known_faces_dir="known_faces"):

        self.known_faces_dir = known_faces_dir

        self.embeddings = []

        self.names = []

        self.app = FaceAnalysis(
            name="buffalo_l",
            providers=["CPUExecutionProvider"]
        )

        self.app.prepare(
            ctx_id=-1,
            det_size=(640, 640)
        )

        self.load_faces()

    def load_faces(self):

        if not os.path.exists(self.known_faces_dir):
            os.makedirs(self.known_faces_dir)

        for file in os.listdir(self.known_faces_dir):

            if not file.lower().endswith(
                (".jpg", ".jpeg", ".png")
            ):
                continue

            image_path = os.path.join(
                self.known_faces_dir,
                file
            )

            image = cv2.imread(image_path)

            if image is None:
                continue

            faces = self.app.get(image)

            if len(faces) == 0:
                print(f"No face found in {file}")
                continue

            self.embeddings.append(
                faces[0].embedding
            )

            self.names.append(
                os.path.splitext(file)[0]
            )

            print(f"Loaded: {file}")

    def get_embeddings(self):
        return self.embeddings

    def get_names(self):
        return self.names