import cv2
import numpy as np
import os

# Load YOLO
net = cv2.dnn.readNet("yolov3_training_2000.weights", "yolov3_testing.cfg")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_DEFAULT)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
classes = ["Weapon", "Knife"]  # Add "Knife" to the list

# Open the video file
cap = cv2.VideoCapture(0)

weapon_count = 0
output_dir = "detected_images"  # Directory to save detected images

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

while True:
    _, img = cap.read()

    if img is None:
        break

    height, width, _ = img.shape

    # Detecting objects
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]

    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    outs = net.forward(output_layers)

    # Showing information on the screen
    class_ids = []
    confidences = []
    boxes = []

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5 and classes[class_id] in ["Weapon", "Knife"]:  # Check for "Weapon" or "Knife"
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_PLAIN

    weapon_count = len(indexes)  # Count of detected weapons

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img, label, (x, y + 30), font, 3, color, 3)

            # Save the detected image
            detected_image = img[y:y + h, x:x + w]
            output_filename = os.path.join(output_dir, f"{label}_{weapon_count}.jpg")
            cv2.imwrite(output_filename, detected_image)

    cv2.putText(img, f"Weapons: {weapon_count}", (20, 50), font, 2, (0, 255, 0), 2)  # Display weapon count

    cv2.imshow("Weapon Detection", img)

    key = cv2.waitKey(1)
    if key == 27:  # Press 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()
