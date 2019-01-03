w = [1, 0, 0, 0, 0, 0, 0, 0, 0]
s = [0, 1, 0, 0, 0, 0, 0, 0, 0]
a = [0, 0, 1, 0, 0, 0, 0, 0, 0]
d = [0, 0, 0, 1, 0, 0, 0, 0, 0]
wa = [0, 0, 0, 0, 1, 0, 0, 0, 0]
wd = [0, 0, 0, 0, 0, 1, 0, 0, 0]
sa = [0, 0, 0, 0, 0, 0, 1, 0, 0]
sd = [0, 0, 0, 0, 0, 0, 0, 1, 0]
nk = [0, 0, 0, 0, 0, 0, 0, 0, 1]


def keys_to_output(input):
    if 'W' in input and 'A' in input:
        output = wa
    elif 'W' in input and 'D' in input:
        output = wd
    elif 'S' in input and 'A' in input:
        output = sa
    elif 'S' in input and 'D' in input:
        output = sd
    elif 'W' in input:
        output = w
    elif 'S' in input:
        output = s
    elif 'A' in input:
        output = a
    elif 'D' in input:
        output = d
    else:
        output = nk

    return output
