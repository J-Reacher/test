import time

import numpy as np
from numba import njit, prange


@njit(parallel=True, fastmath=True)
def test(x):
    n = x.shape[0]
    a = np.sin(x)
    b = np.cos(a * a)
    acc = 0
    for i in prange(n - 2):
        for j in prange(n - 1):
            acc += b[i] + b[j + 1]
    return acc


if __name__ == '__main__':
    start = time.time()

    test(np.arange(10))

    test.parallel_diagnostics(level=4)

    end = time.time()
    print("Time taken:", end - start)
