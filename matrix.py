import numpy as np

def getA():
    A = [[611, 196, -192, 407, -8, -52, -49, 29],
         [0, 899, 113, -192, -71, -43, -8, -44],
         [0, 0, 899, 196, 61, 49, 8, 52],
         [0, 0, 0, 611, 8, 44, 59, -23],
         [0, 0, 0, 0, 411, -599, 208, 208],
         [0, 0, 0, 0, 0, 411, 208, 208],
         [0, 0, 0, 0, 0, 0, 99, -911],
         [0, 0, 0, 0, 0, 0, 0, 99],
         ]

    A = np.array(A)
    for i in range(8):
        for j in range(8):
            if i > j:
                A[i, j] = A[j, i]

    return A

def getB():
    B = np.zeros(shape = (10, 10))

    for i in range(10):
        for j in range(10):
            if i <= j:
                B[i, j] = 1/(i+j+1)

    for i in range(10):
        for j in range(10):
            if i > j:
                B[i, j] = B[j, i]

    return B

def getC():
    C = np.zeros(shape = (12, 12))
    for i in range(12):
        for j in range(12):
            if i == j:
                C[i, j] = 12 - i

    for i in range(12):
        for j in range(12):
            if i > j:
                C[i, j] = C[i, i]
            elif i < j:
                C[i, j] = C[j, j]

    return C

def getD():
    D = np.zeros(shape=(20, 20))
    for i in range(20):
        for j in range(20):
            D[i, j] = np.sqrt(2/21) * np.sin(i * j * np.pi / 21)

    return D

if __name__ == '__main__':
    print(getD())