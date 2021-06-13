import numpy as np
from matrix import getA, getB, getC, getD
from time import *


# 1) 用幂法求矩阵的最大特征值及其特征向量
def power_eng(A):
    '''
    :param A: 需要计算的矩阵
    :return: 成功时返回最大特征值pld和对应的特征向量env
    '''

    # m = None
    # x = None
    n = A.shape[0]

    v = np.ones(n)  # 初始化一个ones向量v作为v_0
    # u = v / v.max()

    # last_m = 0      # 记录上一次的m的值

    for i in range(1000):
        y = v / np.abs(v.max())
        v = np.dot(A, y)
        # y = np.dot(A, v)
        # # print('y', y)
        # m = y.max()
        # x = y / m
        #
        # # print(m)
        # # print(last_m)
        #
        # print(np.abs(m - last_m))
        # # print('y', y)
        # # print('m', m)
        # # print('last_m', last_m)
        #
        # if np.abs(m - last_m) <= 1:
        #     print('i', i)
        #     break
        #
        # v = np.dot(A, v)       # 计算下一个v向量
        # # print('v', v)
        # last_m = m

    pld = v.max()
    env = y

    return pld, env


# 2) 用反幂法求矩阵的最小特征值及其特征向量
def inv_power_eng(A):
    '''
    :param A: 需要计算的矩阵
    :return: 成功时返回最大特征值pld和对应的特征向量env
    '''

    pld, env = power_eng(np.linalg.inv(A))

    return 1/pld, env

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

    # print(np.linalg.eigvals(A).max())
    #
    # print(power_eng(A, 1000))

    # for i, mat in enumerate([A, B, C, D]):
    #     pld, env = power_eng(mat)
    #     st = time()
    #     print('第' + str(i + 1) + '个矩阵最大特征值及其特征向量: ', pld.round(5), env.round(5))
    #     et = time()
    #     max_pld = np.linalg.eigvals(mat).max()
    #     print('第' + str(i + 1) + '个矩阵的最大特征值误差: ', np.abs(max_pld - pld).round(5))
    #     print('runtime: ', et - st)
    #
    #     pld, env = inv_power_eng(mat)
    #     st = time()
    #     print('第' + str(i + 1) + '个矩阵最小特征值及其特征向量: ', pld.round(5), env.round(5))
    #     et = time()
    #     inv_mat = np.linalg.inv(mat)
    #     min_pld = np.linalg.eigvals(inv_mat).min()
    #     # print(min_pld)
    #     print('第' + str(i + 1) + '个矩阵的最小特征值误差: ', np.abs(min_pld - pld).round(5))
    #     print('runtime: ', et - st)

    for i, mat in enumerate([A, B, C, D]):
        pass