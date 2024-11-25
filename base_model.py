from ultralytics import YOLO
import cv2

model = YOLO('yolov10n.pt')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for result in results: 
        for detection in result.boxes.data: 
            x1, y1, x2, y2, conf, cls = detection.tolist()
            class_id = int(cls)

            label = f"{model.names[class_id]} {float(conf):.2f}"

            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

            cv2.putText(frame, label, (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('YOLO Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
