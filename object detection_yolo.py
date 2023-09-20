# import cv2
# from ultralytics import YOLO

# # Load the YOLOv8 model
# model = YOLO('model.pt')

# # Open the video file
# # video_path = "path/to/your/video/file.mp4"
# cap = cv2.VideoCapture(0)

# # Loop through the video frames
# while cap.isOpened():
#     # Read a frame from the video
#     success, frame = cap.read()

#     if success:
#         # Run YOLOv8 inference on the frame
#         results = model(frame)
#         print(results[0])

#         # Visualize the results on the frame
#         annotated_frame = results[0].plot()

#         # Display the annotated frame
#         cv2.imshow("YOLOv8 Inference", annotated_frame)

#         # Break the loop if 'q' is pressed
#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break
#     else:
#         # Break the loop if the end of the video is reached
#         break

# # Release the video capture object and close the display window
# cap.release()
# cv2.destroyAllWindows()




import cv2
from collections import defaultdict
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('model.pt')

# Open the video file
# video_path = "path/to/your/video/file.mp4"
cap = cv2.VideoCapture(0)

# Initialize a dictionary to store object counts
object_counts = defaultdict(int)

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()

    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame)

        # Process detected objects and update counts
        # for label, confidence, bbox in zip(results.names[0], results.xyxy[0][:, 4].tolist(), results.xyxy[0][:, :-1].tolist()):
        #     object_counts[label] += 1

        # Visualize the results on the frame
        annotated_frame = results[0].render()[0]

        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)

        # Display object counts in the console
        # print(object_counts)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
