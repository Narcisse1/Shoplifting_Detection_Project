import cv2
import numpy as np
from tqdm import tqdm

def generate_placeholder_video(filename, width, height, frames, fps, text):
    """Generates a simple placeholder video with moving text."""
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(filename, fourcc, fps, (width, height))

    for i in tqdm(range(frames), desc=f"Generating {filename}"):
        frame = np.zeros((height, width, 3), dtype=np.uint8)
        
        # Simple animation: move text across the screen
        x_pos = int((i * 5) % (width + 200) - 100)
        
        # Draw a simple background to simulate a store
        cv2.rectangle(frame, (0, 0), (width, height // 4), (50, 50, 50), -1)
        cv2.rectangle(frame, (0, height // 4), (width, height), (100, 100, 100), -1)

        # Draw a placeholder "person" (a circle)
        center_x = int(width * 0.5 + 50 * np.sin(i * 0.1))
        center_y = int(height * 0.7)
        cv2.circle(frame, (center_x, center_y), 30, (0, 255, 0), -1)
        
        # Draw the title text
        cv2.putText(frame, text, (x_pos, height // 2), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        # Draw a "Detection Zone" box
        cv2.rectangle(frame, (width//4, height//2), (3*width//4, height), (0, 0, 255), 2)
        cv2.putText(frame, "Detection Zone", (width//4 + 10, height//2 - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

        out.write(frame)

    out.release()

if __name__ == "__main__":
    # Video 1: Normal behavior (for 'control' test)
    generate_placeholder_video(
        filename='shoplifting_project/data/video_normal.mp4',
        width=640, height=480, frames=150, fps=15,
        text='Normal Behavior - Control Test'
    )

    # Video 2: Shoplifting event (for 'anomaly' test)
    generate_placeholder_video(
        filename='shoplifting_project/data/video_shoplifting.mp4',
        width=640, height=480, frames=150, fps=15,
        text='Shoplifting Event - Anomaly Test'
    )

    print("Placeholder videos generated successfully.")
