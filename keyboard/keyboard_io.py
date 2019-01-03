import ctypes
from enum import Enum
import win32api as w_api
from keyboard.misc import Input, InputI, KeyBdInput


class OutputKeys(Enum):
    W = 0x11
    A = 0x1E
    S = 0x1F
    D = 0x20


class KeyboardIO(object):
    def __init__(self):
        self.i_key_list = ['\b']
        self.prepare_ikey_list()
        self.get_keyboard_input()

    def prepare_ikey_list(self):
        for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\":
            self.i_key_list.append(ch)

    def get_keyboard_input(self):
        keys = []
        for k in self.i_key_list:
            if w_api.GetAsyncKeyState(ord(k)):
                keys.append(k)
        return keys

    def press_keys(self, hex_codes):
        for hex_code in hex_codes:
            self.press_key(hex_code.value)  # ENUM -> INT

    @staticmethod
    def press_key(hex_code):
        extra = ctypes.c_ulong(0)
        ii_ = InputI()
        ii_.ki = KeyBdInput(0, hex_code, 0x0008, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

    def release_keys(self, hex_codes):
        for hex_code in hex_codes:
            self.release_key(hex_code.value)  # ENUM -> INT

    @staticmethod
    def release_key(hex_code):
        extra = ctypes.c_ulong(0)
        ii_ = InputI()
        ii_.ki = KeyBdInput(0, hex_code, 0x0008 | 0x0002, 0, ctypes.pointer(extra))
        x = Input(ctypes.c_ulong(1), ii_)
        ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))
