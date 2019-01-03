from keyboard.keyboard_io import OutputKeys as OK


w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]

choice_to_press_key = [[OK.W], [OK.S], [OK.A], [OK.D], [OK.W, OK.A], [OK.W, OK.D], [OK.S, OK.A], [OK.S, OK.D], []]
choice_to_release_key = [
    [OK.S, OK.A, OK.D],         # W
    [OK.W, OK.A, OK.D],         # S
    [OK.S, OK.W, OK.D],         # A
    [OK.S, OK.A, OK.W],         # D
    [OK.S, OK.D],               # WA
    [OK.S, OK.A],               # WD
    [OK.W, OK.D],               # SA
    [OK.W, OK.A],               # SD
    [OK.W, OK.S, OK.A, OK.D]    # NK
]

def keys_to_output(input_0):
    if 'W' in input_0 and 'A' in input_0:
        output = wa
    elif 'W' in input_0 and 'D' in input_0:
        output = wd
    elif 'S' in input_0 and 'A' in input_0:
        output = sa
    elif 'S' in input_0 and 'D' in input_0:
        output = sd
    elif 'W' in input_0:
        output = w
    elif 'S' in input_0:
        output = s
    elif 'A' in input_0:
        output = a
    elif 'D' in input_0:
        output = d
    else:
        output = nk

    return output
