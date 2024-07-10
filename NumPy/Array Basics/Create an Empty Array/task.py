import numpy as np


def create_arrays(x, y):
    # TODO
    a = np.ones([x, y], dtype=int)
    b = np.zeros((y, x), dtype=bool)
    return a, b


if __name__ == '__main__':
    arrays = create_arrays(3, 4)
    print('\narray of int using ones:')
    print(arrays[0])
    print(f'dtype: {arrays[0].dtype}')
    print('\nTrue Boolean Array using .full:')
    print(arrays[1])
    print(f'dtype: {arrays[1].dtype}')

    print(arrays[0].shape)
