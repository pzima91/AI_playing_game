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


class Trainer(object):
    def __init__(self):
        self.filename = '{}.npy'.format(int(time.time()))
        self.keyboard = KeyboardIO()

        print('TRAINER CREATED, filename: {}'.format(self.filename))

        if self.collect_data():
            self.fit_model()

    def collect_data(self):
        for i in range(5):
            print('TRAINER START IN : {}'.format(5 - i))
            time.sleep(1.0)

        training_data = []

        while True:
            screen = grab_screen(region=imaging_config.grab_screen_region)
            screen = cv2.resize(screen, imaging_config.grab_screen_r_size)
            keys = self.keyboard.get_keyboard_input()

            # PREVIEW WINDOw
            cv2.imshow(imaging_config.preview_window_name, screen)
            cv2.waitKey(1)

            if 'N' in keys:
                cv2.destroyAllWindows()
                print('TRAINER STOPPED WITHOUT FIT')
                return False

            if 'M' in keys:
                cv2.destroyAllWindows()
                print('TRAINER STOPPED WITH FIT')
                return True

            normalized_keys = map.keys_to_output(keys)
            print('{} - {}'.format(len(training_data), str(normalized_keys)))

            training_data.append([screen, normalized_keys])
            if len(training_data) % training_config.training_data_save_mod == 0:
                np.save(self.filename, training_data)
                print('{} - SAVE...'.format(len(training_data)))

    @staticmethod
    def print_decision_dict_info(decision_dict):
        for key in decision_dict.keys():
            print('\t{} - {} elements.'.format(str(key), str(len(decision_dict[str(key)]))))

    def balance_data(self):
        non_balanced_data = np.load(self.filename)
        print('DATA LEN BEFORE BALANCING: {}'.format(len(non_balanced_data)))

        random.shuffle(non_balanced_data)

        decision_dict = {}
        for data in non_balanced_data:
            if str(data[1]) in decision_dict.keys():
                decision_dict[str(data[1])].append(data)
            else:
                decision_dict[str(data[1])] = []
                decision_dict[str(data[1])].append(data)

        self.print_decision_dict_info(decision_dict)

        total_len = len(non_balanced_data)
        mean_len = int(total_len / len(decision_dict.keys()))

        mean_balanced_data = []
        for key in decision_dict.keys():
            decision_dict[key] = decision_dict[key][:mean_len]
            mean_balanced_data = mean_balanced_data + decision_dict[key]

        print('DATA LEN AFTER BALANCING: {}'.format(len(mean_balanced_data)))
        self.print_decision_dict_info(decision_dict)

        random.shuffle(mean_balanced_data)
        return mean_balanced_data

    def fit_model(self):
        data = self.balance_data()

        model = alex(imaging_config.grab_screen_r_width, imaging_config.grab_screen_r_height,
                     training_config.training_learning_rate, output=9)

        training_data, test_data = data[:int(len(data) / 2)], data[int(len(data) / 2):]

        training_data_x = np.array([i[0] for i in training_data]).reshape(
            -1, imaging_config.grab_screen_r_width, imaging_config.grab_screen_r_height, 1
        )
        training_data_y = [i[1] for i in training_data]

        test_data_x = np.array([i[0] for i in test_data]).reshape(
            -1, imaging_config.grab_screen_r_width, imaging_config.grab_screen_r_height, 1
        )
        test_data_y = [i[1] for i in test_data]

        model.fit({'input': training_data_x}, {'targets': training_data_y},
                  validation_set=({'input': test_data_x}, {'targets': test_data_y}),
                  n_epoch=training_config.training_epochs,
                  snapshot_step=training_config.training_snapshot_step,
                  show_metric=True,
                  run_id=training_config.training_model_name)

        model.save(training_config.training_model_name)

        return 0
