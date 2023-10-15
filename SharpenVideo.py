import cv2
import numpy as np

def sharpen_frame(frame):
    # Define the sharpening kernel
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    
    # Apply the kernel to the frame
    sharpened_frame = cv2.filter2D(frame, -1, kernel)
    
    return sharpened_frame

# Input and output video file paths
input_video_path = 'input.mp4'
output_video_path = 'output_video(sharpen).mp4'

# Open the input video file
input_video = cv2.VideoCapture(input_video_path)

# Get the video's width, height, and FPS
width = int(input_video.get(3))
height = int(input_video.get(4))
fps = int(input_video.get(5))

# Define the VideoWriter to save the sharpened video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while True:
    ret, frame = input_video.read()
    if not ret:
        break

    # Sharpen the frame
    sharpened_frame = sharpen_frame(frame)

    # Write the sharpened frame to the output video
    output_video.write(sharpened_frame)

# Release the video objects
input_video.release()
output_video.release()

# Destroy any OpenCV windows
cv2.destroyAllWindows()
