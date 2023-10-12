import cv2
from ..config import video_location

def display_video(video_location):
    """_summary_

    Args:
        video_location (_type_): _description_
    """
    # Open the video capture object
    cap = cv2.VideoCapture(video_location)

    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file")
    else:
        while True:
            # Read a frame from the video
            ret, frame = cap.read()
            
            if not ret:
                print("End of video")
                break
            
            # Display the frame
            cv2.imshow("Video", frame)

            # Break the loop if the 'q' key is pressed
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

        # Release the video capture object and close the display window
        cap.release()
        cv2.destroyAllWindows()

# Call the display_video function with the video_location
display_video(video_location)
