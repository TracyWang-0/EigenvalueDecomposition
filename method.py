import numpy as np
from matrix import getA, getB, getC, getD

# 1) 用幂法求矩阵的最大特征值及其特征向量
def power_eng(a):
    '''
    :param a: 需要计算的矩阵
    :return: 成功时返回最大特征值pld和特征向量env；失败时返回串failed
    '''

    pld = None
    env = None
    failed = "失败"
    n = a.shape[0]

    return pld, env

# 2) 用反幂法求矩阵的最小特征值及其特征向量
def inv_power_eng(a):
    '''
    :param a: 需要计算的矩阵
    :return: 成功时返回最小特征值pld和特征向量env；失败时返回串failed
    '''

    pld = None
    env = None
    failed = "失败"
    n = a.shape[0]

    return pld, env

# 3) 用Jacobi方法求对称矩阵的全部特征值
def jacobi_eng(a):
    '''
    :param a: 需要计算的矩阵
    :return: 成功时返回特征值ev；失败时返回串failed
    '''

    ev = None
    failed = "失败"
    n = a.shape[0]

    return ev

# 4) 用Gauss相似变换将矩阵就地转换为上Hessenberg矩阵
def gauss_hessen(a):
    '''
    :param a: 需要计算的矩阵
    :return: 返回上Hessenberg矩阵
    '''

    n = a.shape[0]
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


    pass


