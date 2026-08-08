from recognition.database import FaceDatabase
from recognition.matcher import FaceMatcher


class FaceRecognizer:

    def __init__(self):

        self.database = FaceDatabase()

        self.matcher = FaceMatcher()

    def recognize(self, face_encodings):

        results = []

        known_encodings = self.database.get_encodings()

        known_names = self.database.get_names()

        for encoding in face_encodings:

            name = self.matcher.match(
                encoding,
                known_encodings,
                known_names
            )

            results.append(name)

        return results