#q1
import cv2
import re
import matplotlib.pyplot as plt
import pytesseract
from PIL import Image
from pathlib import Path

image_path = input("Enter medicine bottle image path: ").strip()
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Image not found. Check the file path.")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
processed = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
text = pytesseract.image_to_string(processed)

print("Extracted label text:")
print(text)

medicine_name = re.search(r"(?im)^(?:medicine|drug|product)?\s*name\s*[:\-]?\s*(.+)$", text)
dosage = re.search(r"(?i)\b\d+(?:\.\d+)?\s*(?:mg|mcg|g|ml|%)\b", text)
expiry = re.search(r"(?i)(?:exp(?:iry)?\.?\s*date?\s*[:\-]?\s*)(\d{1,2}[/-]\d{2,4}|\d{2,4}[/-]\d{1,2})", text)
batch = re.search(r"(?i)(?:batch|lot)\s*(?:no\.?|number)?\s*[:\-]?\s*([A-Z0-9-]+)", text)

print("\nPossible medicine name:", medicine_name.group(1).strip() if medicine_name else "Not detected")
print("Possible dosage:", dosage.group(0) if dosage else "Not detected")
print("Possible expiry date:", expiry.group(1) if expiry else "Not detected")
print("Possible batch number:", batch.group(1) if batch else "Not detected")

plt.figure(figsize=(8, 6))
plt.imshow(rgb_image)
plt.axis("off")
plt.show()

#q2
from pathlib import Path
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

image_path = input("Enter face image path: ").strip()
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Image not found. Check the file path.")

rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
result = DeepFace.analyze(
    img_path=image,
    actions=["emotion"],
    enforce_detection=False,
    detector_backend="opencv"
)

if isinstance(result, list):
    faces = result
else:
    faces = [result]

for index, face in enumerate(faces, start=1):
    emotion = face.get("dominant_emotion", "unknown")
    scores = face.get("emotion", {})
    print(f"Face {index}: {emotion}")
    print("Emotion scores:", scores)

    region = face.get("region", {})
    x = int(region.get("x", 0))
    y = int(region.get("y", 0))
    w = int(region.get("w", 0))
    h = int(region.get("h", 0))

    if w > 0 and h > 0:
        cv2.rectangle(rgb_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(
            rgb_image,
            emotion,
            (x, max(y - 10, 20)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

plt.figure(figsize=(8, 6))
plt.imshow(rgb_image)
plt.axis("off")
plt.show()
