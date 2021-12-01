from sympy import *
from sympy.core.symbol import Symbol
from sympy import init_printing
import numpy as np
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

init_printing(use_unicode=True)

x1 = Symbol('x1')   # 初始化变量
x2 = Symbol('x2')   # 初始化变量

y = (1/2) * (2*x1**2 + 8*x2**2)     # 输入函数关系式，函数的次数不能超过二次
X0 = np.array([[1], [1]])           # 给定X的初始值
m = 0.0001                           # 给定精度
max_i = 1000                        # 给定最大迭代次数

def calculate(X0, y, max_i):
    X_i = X0

    gx1 = diff(y, x1)   # 对函数求梯度
    gx2 = diff(y, x2)   # 对函数求梯度

    q11 = diff(gx1, x1) # 对函数二阶求导
    q12 = diff(gx1, x2) # 对函数二阶求导
    q21 = diff(gx2, x1) # 对函数二阶求导
    q22 = diff(gx2, x2) # 对函数二阶求导
    Q = [[q11, q12], [q21, q22]]    # Hessian矩阵

    data = []
    data_x = []
    data_y = []
    data_z = []

    for i in range(max_i):      # 最速下降法最大迭代次数
        g_i = [[gx1.evalf(subs={x1: X_i[0][0], x2: X_i[1][0]})],
               [gx2.evalf(subs={x1: X_i[0][0], x2: X_i[1][0]})]]  

        g_i = np.array(g_i, dtype=np.float32) 
        gT_i = np.transpose(g_i)          # 将g(i)进行转置  
        p_i = -1 * g_i                    # 求得p(i)
        pT_i = np.transpose(p_i)          # 将p(i)进行转置

        distance = sqrt((p_i[0][0]**2) + ((p_i[1][0]**2)))     # 对p(i)求模
        Y = y.evalf(subs={x1: X_i[0][0], x2: X_i[1][0]})    # 输出函数极小值
        data_x.append(X_i[0][0])
        data_y.append(X_i[1][0])
        data_z.append(Y)

        if distance < m :       # 如果计算p(i)的模小于精度，则迭代达到要求，否则继续迭代
            data.append([data_x, data_y, data_z])
            return X_i, Y, data

        lam_i = -1 * np.dot(gT_i, p_i) / np.dot(np.dot(pT_i, Q), p_i)   # 求得lamba
        X_i = X_i + lam_i * p_i           # 更新X(i)

    data.append([data_x, data_y, data_z])
    return X_i, Y, data

if __name__ == '__main__':
    X_min, Y_min, data = calculate(X0, y, max_i)

    # 画图
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(data[0][0], data[0][1], data[0][2], label='parametric curve')
    ax.legend()
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_zlabel('Y')
    plt.show()
    
    

