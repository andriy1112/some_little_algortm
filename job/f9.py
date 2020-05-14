import numpy as np


def matrix_transponse(m):
    arr1 = np.array(m)
    return arr1.transpose()


m = [[23, 56, 44],
     [70, 56, 77],
     [26, 27, 10]]

t = matrix_transponse(m)
print('\n'.join(str(r) for r in t))