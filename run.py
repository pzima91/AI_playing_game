from keyboard.keyboard_io import KeyboardIO
from config import imaging_config
from ai.trainer import Trainer
from ai.tester import Tester
import time
import cv2

cv2.namedWindow(imaging_config.preview_window_name)

keyboard = KeyboardIO()

print('STARTED')
while True:
    keys = keyboard.get_keyboard_input()

    if 'J' in keys:
        # instance = Trainer()
        instance = Tester()

    time.sleep(0.1)
