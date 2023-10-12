import cv2
from ..config import video_location
from src.data_layer.load_video import display_video

def enhance_video(video_location):
    """_summary_

    Args:
        video_location (_type_): _description_
    """
    # Open the video capture object
    cap = cv2.VideoCapture(video_location)

    if not cap.isOpened():
        print("Error: Could not open video file")
    else:
        # Define a VideoWriter to save the enhanced video to a temporary file
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('enhanced_video.avi', fourcc, 20.0, (640, 480))  

        while True:
            ret, frame = cap.read()

            if not ret:
                print("End of video")
                break

            # Apply noise reduction (e.g., Gaussian blur)
            frame = cv2.GaussianBlur(frame, (5, 5), 0)

            # Apply contrast adjustment (e.g., increase contrast)
            alpha = 1.5  
            frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=0)

            # Write the enhanced frame to the original video
            out.write(frame)

        cap.release()
        out.release()
        cv2.destroyAllWindows()

        # Call the display_video function with the path to the enhanced video
        display_video(video_location)

enhance_video(video_location)

