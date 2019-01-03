from keyboard.keyboard_io import KeyboardIO
from config import imaging_config
from ai.trainer import Trainer
import time
import cv2


keyboard = KeyboardIO()

print('STARTED')
while True:
    keys = keyboard.get_keyboard_input()

    if 'J' in keys:
        instance = Trainer()

    time.sleep(0.1)
