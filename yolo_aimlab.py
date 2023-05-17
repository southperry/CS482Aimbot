from ultralytics import YOLO
import keyboard
import time
from PIL import ImageGrab
import numpy as np
import win32api, win32con

if __name__ == "__main__":
    # Import pre-trained YOLO model for Aim Lab's Gridshot
    yolo = YOLO(model="../models/yolo_aimlab.pt")
    # Wait for user to press E key to start the bot
    while True:
        if keyboard.is_pressed('e'):
            print("starting")
            break
    while True:
        # The bot is running! If the user presses R during the bot running, stop it all
        if keyboard.is_pressed('r'):
            break
        # Get the prediction from the YOLO model based on our screenshot
        results = yolo.predict(np.array(ImageGrab.grab()))
        # Check if there's any predicted targets on screen
        if len(results) != 0:
            # If there is, get the list of bounding boxes of said targets
            boxes = results[0].boxes
            # Make sure there really is at least one target's bounding box available
            if (len(boxes) != 0):
                # There is! Get the bounding box of it
                bb = boxes[0].xyxy.numpy()[0]

                # Calculate the center of the bounding box (and hence the center of the target)
                x = (int(bb[2]) - int(bb[0])) // 2 + int(bb[0])
                y = (int(bb[3]) - int(bb[1])) // 2 + int(bb[1])

                # Get the current mouse coordinates
                mouse_x, mouse_y = win32api.GetCursorPos()

                # Calculate the difference between where the mouse is and where the target is
                delta_x = int(x - mouse_x)
                delta_y = int(y - mouse_y)

                # Use this difference to move the mouse by that much (relative to its current location), and click there
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, delta_x, delta_y, 0, 0)
                time.sleep(0.0001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, delta_x, delta_y, 0, 0)
                time.sleep(0.0001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, delta_x, delta_y, 0, 0)