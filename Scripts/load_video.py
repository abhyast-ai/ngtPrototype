# import all required libraries
import cv2
import os

# set the path to the required sample video location

# Get the current directory
current_directory = os.getcwd()

# Move up one level from the current directory
parent_directory = os.path.dirname(current_directory)

# Specify the folder and file name
video_location = os.path.join(parent_directory, "ngtPrototype", "Data", "sample.mp4")

# Check if the file exists
if os.path.isfile(video_location):
    # use the video location to load the video here
    cap = cv2.VideoCapture(video_location)  # For a video file
    # cap = cv2.VideoCapture(0) For the default camera

    while True:
        ret, frame = cap.read()  # Read a frame from the video capture

        if not ret:
            break  # Break the loop if no frames are left

        # Apply noise reduction (e.g., Gaussian blur)
        frame = cv2.GaussianBlur(frame, (5, 5), 0)

        # Apply contrast adjustment (e.g., increase contrast)
        alpha = 1.5  # Adjust this value to change the contrast
        frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=0)

        cv2.imshow("Video", frame)  # Display the frame in a window named 'Video'

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break  # Exit the loop if 'q' key is pressed or use Esc key
    cap.release()
    cv2.destroyAllWindows()

else:
    print("The video file does not exist.")
