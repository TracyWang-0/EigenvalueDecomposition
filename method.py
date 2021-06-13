import numpy as np
from matrix import getA, getB, getC, getD

# 1) 用幂法求矩阵的最大特征值及其特征向量
def power_eng(A):
    '''
    :param A: 需要计算的矩阵
    :return: 成功时返回最大特征值m和特征向量x
    '''

    m = None
    x = None
    n = A.shape[0]

    v = np.zeros(n)     # 初始化一个one-hot向量v作为随机向量
    v[-1] = 1

    last_m = 0      # 记录上一次的m的值

    while True:
        y = A * v
        y = y[:, -1]
        m = max(y)
        x = y / m

        if m - last_m <= 1e-6:
            break

        v = A * v       # 计算下一个v向量

    return m, x

# 2) 用反幂法求矩阵的最小特征值及其特征向量
def inv_power_eng(A):
    '''
    :param A: 需要计算的矩阵
    :return: 成功时返回最小特征值m和特征向量x
    '''

    return power_eng(np.linalg.inv(A))

# 3) 用Jacobi方法求对称矩阵的全部特征值
def jacobi_eng(A):
    '''
    :param A: 需要计算的矩阵
    :return: 成功时返回特征值ev；失败时返回串failed
    '''

    ev = None
    failed = "失败"
    n = A.shape[0]

    return ev

# 4) 用Gauss相似变换将矩阵就地转换为上Hessenberg矩阵
def gauss_hessen(A):
    '''
    :param A: 需要计算的矩阵
    :return: 返回上Hessenberg矩阵
    '''

    n = A.shape[0]
    Hessenberg = None

    return Hessenberg

# 5) 矩阵特征值问题QR算法辅助函数
def qr_aux(i, j):
    '''
    :param i:
    :param j:
    :return:
    '''
    pass

if __name__ == '__main__':
    A = getA()
    B = getB()
    C = getC()
    D = getD()
    for mat in [A, B, C, D]:
        print('矩阵' + str(mat) + '最大特征值及其特征向量: ', power_eng(mat))
        print('矩阵' + str(mat) + '最小特征值及其特征向量: ', inv_power_eng(mat))




