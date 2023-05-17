import pyautogui
import keyboard
import time
from PIL import ImageGrab
import win32api, win32con

pyautogui.PAUSE = 0.01

if __name__ == "__main__":
    preparing = True
    tl_set = False
    br_set = False
    running = False

    while preparing:
        # Wait for user to press Q key to define the top-left of the region used by the game (This helps avoid UI elements)
        if keyboard.is_pressed('q'):
            top_left = pyautogui.position()
            tl_set = True
            print("Top left set to " + str(top_left))
        # Wait for user to press W key to define the bottom-right of the region used by the game
        if keyboard.is_pressed('w'):
            bottom_right = pyautogui.position()
            br_set = True
            print("Bottom right set to " + str(top_left))
        if tl_set and br_set:
            # Wait for user to press E key to start the bot
            if keyboard.is_pressed('e'):
                print("Starting color bot")
                preparing = False
                running = True
    while True:
        # The bot is running! If the user presses R during the bot running, stop it all
        if keyboard.is_pressed('r'):
            print("stopping")
            break
        # Take a screenshot of the main monitor
        screenshot = ImageGrab.grab()
        # Loop over the pixels in the screenshot from top-left to bottom-right, skipping 4 pixels each iteration
        for x in range(top_left.x, bottom_right.x, 4):
            for y in range(top_left.y, bottom_right.y, 4):
                # Get the RGB values of the current pixel
                r, g, b = screenshot.getpixel((x, y))
                # Check if the pixel is either pure white or a specific shade of orange
                # (both of these RGB values are used by the targets)
                if (r == 255 and g == 87 and b == 34) or (r == 255 and g == 255 and b == 225):
                    # If so, get the mouse's current position
                    mouse_x, mouse_y = win32api.GetCursorPos()

                    # Calculate the difference between the current position of the mouse, and where the pixel is on screen
                    delta_x = int(x - mouse_x)
                    delta_y = int(y - mouse_y)

                    # Use the calculated difference to move the mouse by that amount, and then click there
                    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, delta_x, delta_y, 0, 0)
                    time.sleep(0.0001)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, delta_x, delta_y, 0, 0)
                    time.sleep(0.0001)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, delta_x, delta_y, 0, 0)
                    # Get out of the loop! Since we moved the mouse and clicked, all of the targets are now
                    # in different places on-screen. We'll need to start again.
                    break
            else:
                continue
            break