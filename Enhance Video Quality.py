import cv2

# Input and output video file paths
input_video_path = 'input.mp4'
output_video_path = 'output_video.mp4'

# Open the input video file
input_video = cv2.VideoCapture(input_video_path)

# Get the current frame's width and height
width = int(input_video.get(3))
height = int(input_video.get(4))

# Define the desired output resolution
new_width = 7680  # New width in pixels
new_height = 4320  # New height in pixels

# Define the VideoWriter to save the upscaled video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output_video = cv2.VideoWriter(output_video_path, fourcc, 30.0, (new_width, new_height))

while True:
    ret, frame = input_video.read()
    if not ret:
        break

    # Resize the frame to the new resolution
    frame = cv2.resize(frame, (new_width, new_height))

    # Write the frame to the output video
    output_video.write(frame)

# Release the video objects
input_video.release()
output_video.release()

# Destroy any OpenCV windows
cv2.destroyAllWindows()
