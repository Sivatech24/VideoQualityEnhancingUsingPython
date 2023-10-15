import cv2

# Input and output video file paths
input_video_path = 'input.mp4'
output_video_path = 'output_video.mp4'

# Open the input video file
input_video = cv2.VideoCapture(input_video_path)

# Get the current frame rate
current_fps = int(input_video.get(cv2.CAP_PROP_FPS))

# Define the desired output frame rate
new_fps = 90  # New frame rate

# Define the VideoWriter to save the video with the new frame rate
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_video_path, fourcc, new_fps,(int(input_video.get(3)), int(input_video.get(4))))

while True:
    ret, frame = input_video.read()
    if not ret:
        break

    # Write each frame multiple times to increase the frame rate
    for _ in range(new_fps // current_fps):
        output_video.write(frame)

# Release the video objects
input_video.release()
output_video.release()

# Destroy any OpenCV windows
cv2.destroyAllWindows()
