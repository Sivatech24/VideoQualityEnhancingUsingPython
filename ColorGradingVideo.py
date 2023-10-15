import cv2
import numpy as np

def apply_color_grading(frame, brightness=1.0, contrast=1.0, saturation=1.0):
    # Adjust brightness, contrast, and saturation
    frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness * 255)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame = np.array(frame, dtype=np.float32)
    frame[:, :, 1] *= saturation
    frame = np.clip(frame, 0, 255)
    frame = np.array(frame, dtype=np.uint8)
    frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    return frame

# Input and output video file paths
input_video_path = 'input.mp4'
output_video_path = 'output_video(ColorGraded).mp4'

# Open the input video file
input_video = cv2.VideoCapture(input_video_path)

# Get the video's width, height, and FPS
width = int(input_video.get(3))
height = int(input_video.get(4))
fps = int(input_video.get(5))

# Define color grading parameters
brightness = 1.0  # Adjust as needed (1.0 is neutral)
contrast = 1.0   # Adjust as needed (1.0 is neutral)
saturation = 1.0  # Adjust as needed (1.0 is neutral)

# Define the VideoWriter to save the color-graded video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while True:
    ret, frame = input_video.read()
    if not ret:
        break

    # Apply color grading to the frame
    graded_frame = apply_color_grading(frame, brightness, contrast, saturation)

    # Write the graded frame to the output video
    output_video.write(graded_frame)

# Release the video objects
input_video.release()
output_video.release()

# Destroy any OpenCV windows
cv2.destroyAllWindows()
