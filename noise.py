import numpy as np


def noise(input):
    output = ''
    for i in range(len(input)):
        r = np.random.rand()
        if r < 0.1:
            output += '1' if input[i] == '0' else '0'
        else:
            output += input[i]
    # output = input
    return output

