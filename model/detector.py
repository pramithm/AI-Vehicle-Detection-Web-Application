from ultralytics import YOLO
import cv2

# Load model
model = YOLO("yolov8n.pt")

def detect_objects():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]

                # Mapping
                if label == "person":
                    category = "Human"
                elif label == "motorcycle":
                    category = "2 Wheeler"
                elif label == "car":
                    category = "4 Wheeler"
                elif label in ["bus", "truck"]:
                    category = "6 Wheeler"
                else:
                    continue

                # Coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Shrink box (optional)
                shrink = 10
                x1 += shrink
                y1 += shrink
                x2 -= shrink
                y2 -= shrink

                # Draw rectangle
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                # Label text
                conf = float(box.conf[0])
                label_text = f"{category} {conf:.2f}"

                # Get text size
                (w, h), _ = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)

                # Draw filled rectangle (background)
                cv2.rectangle(frame, (x1, y1 - h - 10), (x1 + w, y1), (0, 255, 0), -1)

                # Put text
                cv2.putText(frame, label_text, (x1, y1 - 5),
                               cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

                print(category)

        cv2.imshow("Detection", frame)

        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

# Run function
detect_objects()