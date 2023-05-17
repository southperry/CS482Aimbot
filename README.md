# Computer Vision Aimbot
Aimbots for aimtrainer.io & Aim Lab's Grid Shot, using multiple methods.

## Installation
* Navigate to this folder directory using `cd`
* Run `python -m venv env` to create a virtual environment
* Run one of the following depending on your OS
    * `source env/bin/activate` (Mac/Linux)
    * `.\env\Scripts\activate` (Windows)
* Run `pip install -r requirements.txt` to install all the dependencies

## Usage (After installation!)
* Ensure your screen resolution is 1920x1080 or under (that exact resolution works best!)
* Also ensure scaling is set to 100% (Under Settings > Display .. "Scale and layout" on Windows 10).
* Navigate to this folder directory using `cd`
* Run one of the following depending on your OS
    * `source env/bin/activate` (Mac/Linux)
    * `.\env\Scripts\activate` (Windows)
* Choose which method and scenario you'd like to test, and run the relavent python script:
    * Color Matching Bot
        * Aim Lab: `python color_bot_aimlab.py`
        * aimtrainer.io: `python color_bot_aimtrainerio.py`
    * YOLO Bot
        * Aim Lab: `python yolo_aimlab.py`
        * aimtrainer.io: `python yolo_aimtrainerio.py`
* REQUIRED COLOR BOT ON AIMTRAINER.IO ONLY:
    * Press Q while your mouse is positioned over the top left corner of the game, excluding UI elements such as the time or life count.
    * Then press W with your mouse at the bottom right of the game.
* Controls:
    * Press E to start the bot
    * Press R to stop the bot