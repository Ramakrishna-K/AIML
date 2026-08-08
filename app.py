

import os
import cv2
import numpy as np

from insightface.app import FaceAnalysis

from config import KNOWN_FACES_DIR, CAMERA_INDEX


# ------------------------------------
# Load InsightFace Model
# ------------------------------------

app = FaceAnalysis(
    name="buffalo_l",
    providers=["CPUExecutionProvider"]
)

app.prepare(
    ctx_id=-1,
    det_size=(640, 640)
)


# ------------------------------------
# Load Known Faces
# ------------------------------------

known_embeddings = []
known_names = []

print("Loading known faces...")

for filename in os.listdir(KNOWN_FACES_DIR):

    if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
        continue

    image_path = os.path.join(
        KNOWN_FACES_DIR,
        filename
    )

    image = cv2.imread(image_path)

    faces = app.get(image)

    if len(faces) == 0:
        print(f"No face found in {filename}")
        continue

    embedding = faces[0].embedding

    known_embeddings.append(embedding)

    known_names.append(
        os.path.splitext(filename)[0]
    )

print("Known Faces:", known_names)


# ------------------------------------
# Open Camera
# ------------------------------------

cap = cv2.VideoCapture(CAMERA_INDEX)

THRESHOLD = 0.55

while True:

    success, frame = cap.read()

    if not success:
        break

    faces = app.get(frame)

    for face in faces:

        embedding = face.embedding

        name = "Unknown"

        if len(known_embeddings) > 0:

            similarities = []

            for known in known_embeddings:

                similarity = np.dot(
                    embedding,
                    known
                ) / (
                    np.linalg.norm(embedding)
                    * np.linalg.norm(known)
                )

                similarities.append(similarity)

            best_index = np.argmax(similarities)

            if similarities[best_index] > THRESHOLD:

                name = known_names[best_index]

        box = face.bbox.astype(int)

        x1, y1, x2, y2 = box

        cv2.rectangle(
            frame,
            (x1, y1),
            (x2, y2),
            (0, 255, 0),
            2
        )

        cv2.rectangle(
            frame,
            (x1, y2 - 35),
            (x2, y2),
            (0, 255, 0),
            cv2.FILLED
        )

        cv2.putText(
            frame,
            name,
            (x1 + 8, y2 - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

    cv2.imshow(
        "Face Recognition",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()

cv2.destroyAllWindows()
