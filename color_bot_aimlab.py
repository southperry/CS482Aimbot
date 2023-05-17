import pyautogui
import keyboard
import time
from PIL import ImageGrab
import win32api, win32con

pyautogui.PAUSE = 0.01
offset = 4
skip = 30

while True:
    # Wait for user to press E key to start the bot
    if keyboard.is_pressed('e'):
        print("starting")
        break
while True:
    # The bot is running! If the user presses R during the bot running, stop it all
    if keyboard.is_pressed('r'):
        print("stopping")
        break
    # Take a screenshot of the main monitor
    screenshot = ImageGrab.grab()
    # Loop over the pixels in the screenshot from top-left to bottom-right, skipping "skip" pixels each iteration
    for x in range(0, screenshot.width, skip):
        for y in range(0, int(2.5 * (screenshot.height / 3)), skip): # Avoid clicking on similar-colored elements in the image like the hand and floor by ignoring the bottom 3rd of the screen
            # Get the RGB values of the current pixel
            r, g, b = screenshot.getpixel((x, y))
            # Check if said values create a value that is somewhat similar to the main shade of blue in the targets
            if (r <= 36 and g <= 254 and b <= 255) and (r >= 17 and g >= 144 and b >= 169):
                # If so, get the mouse's current position
                mouse_x, mouse_y = win32api.GetCursorPos()

                # Calculate the difference between the current position of the mouse, and where the pixel is on screen
                delta_x = int(x - mouse_x)
                delta_y = int(y - mouse_y)

                # Use the calculated difference to move the mouse by that amount, and then click there
                win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, delta_x, delta_y, 0, 0)
                time.sleep(0.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, delta_x, delta_y, 0, 0)
                time.sleep(0.001)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, delta_x, delta_y, 0, 0)
                # Get out of the loop! Since we moved the mouse and clicked, all of the targets are now
                # in different places on-screen. We'll need to start again.
                break
        else:
            continue
        break