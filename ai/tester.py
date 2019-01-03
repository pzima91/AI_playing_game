from keyboard.keyboard_io import KeyboardIO
from imaging.grabscreen import grab_screen
from ai.models import alexnet as alex
from config import training_config
from config import imaging_config
from keyboard import map
import numpy as np
import random
import time
import cv2


class Tester(object):
    def __init__(self):
        self.run = False
        self.keyboard = KeyboardIO()
        self.model = alex(imaging_config.grab_screen_r_width, imaging_config.grab_screen_r_height,
                          training_config.training_learning_rate, output=9)
        self.model.load(training_config.training_model_name)

        print('TESTER CREATED')
        self.test_behaviour()

    def test_behaviour(self):
        while True:
            screen = grab_screen(region=imaging_config.grab_screen_region)
            screen = cv2.resize(screen, imaging_config.grab_screen_r_size)
            keys = self.keyboard.get_keyboard_input()

            # PREVIEW WINDOW
            cv2.imshow(imaging_config.preview_window_name, screen)
            cv2.waitKey(1)

            if self.run:
                prediction = self.model.predict([
                    screen.reshape(
                        imaging_config.grab_screen_r_width,
                        imaging_config.grab_screen_r_height,
                        1)
                ])[0]

                print(prediction)
                choice = np.argmax(prediction)

                self.keyboard.press_keys(map.choice_to_press_key[choice])
                self.keyboard.release_keys(map.choice_to_release_key[choice])

            if 'N' in keys and self.run:
                self.run = False
                print('TESTER STOPPED')
            if 'J' in keys and not self.run:
                self.run = True
                print('TESTER STARTED')
            if 'Q'in keys:
                break

