
import numpy as np


class FaceMatcher:

    def __init__(self, threshold=0.55):
        self.threshold = threshold

    def cosine_similarity(
        self,
        embedding1,
        embedding2
    ):

        return np.dot(
            embedding1,
            embedding2
        ) / (
            np.linalg.norm(embedding1)
            * np.linalg.norm(embedding2)
        )

    def match(
        self,
        face_embedding,
        known_embeddings,
        known_names
    ):

        if len(known_embeddings) == 0:
            return "Unknown"

        similarities = []

        for embedding in known_embeddings:

            similarity = self.cosine_similarity(
                face_embedding,
                embedding
            )

            similarities.append(similarity)

        best_match = np.argmax(similarities)

        if similarities[best_match] >= self.threshold:
            return known_names[best_match]

        return "Unknown"