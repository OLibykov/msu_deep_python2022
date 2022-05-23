import ctypes
from typing import List
import time
import random


def multip(arr1: List[int], m, n, arr2: List[int], k, p) -> int:

    lib = ctypes.CDLL("./libutils.so")
    lib.arr.argstype = [
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_int,
        ctypes.c_int,
        ctypes.POINTER(ctypes.c_int),
        ctypes.c_int,
        ctypes.c_int,
    ]

    arr1_type = ctypes.c_int * (m * n)
    arr2_type = ctypes.c_int * (k * p)

    lib.arr(
        arr1_type(*arr1),
        ctypes.c_int(m),
        ctypes.c_int(n),
        arr2_type(*arr2),
        ctypes.c_int(k),
        ctypes.c_int(p),
    )


if __name__ == "__main__":

    A = []
    B = []
    for i in range(40000):
        A.append(random.randint(0, 9))
        B.append(random.randint(0, 9))

    C = [0] * 40000

    t1 = time.time()

    for i in range(200):
        for j in range(200):
            C[i * 200 + j] = 0
            for c in range(200):
                C[i * 200 + j] += A[i * 200 + c] * B[c * 200 + j]

    t2 = time.time()

    f = open("mul_py", "w")
    for i in C:
        f.write(str(i) + " ")
    f.close()

    print(t2 - t1)

    multip(A, 200, 200, B, 200, 200)
