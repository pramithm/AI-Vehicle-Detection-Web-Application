# Video streaming logic
import cv2
from ultralytics import YOLO

model = YOLO("model/yolov8n.pt")

def generate_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        results = model(frame)

        for r in results:
            for box in r.boxes:
                cls = int(box.cls[0])
                label = model.names[cls]
                conf = float(box.conf[0])

                if conf < 0.5:
                    continue

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

                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Draw
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                text = f"{category} {conf:.2f}"
                cv2.putText(frame, text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        # Convert frame to JPEG
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')