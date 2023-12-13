import numpy as np
from scipy.optimize import least_squares

# x nas funções é um vetor pois na realidade, cada posição desse vetor corresponde a uma variável

# FUNÇÕES

def func_1__duas_equacoes(x):
    f1 = x[0]**2 + x[1]**2 - 25
    f2 = x[0]*x[1] - 6
    return np.array([f1, f2])

def func_1__tres_equacoes(x):
    f1 = x[0] + x[1] + x[2] - 6
    f2 = x[0] * x[1] + x[1] * x[2] + x[2] * x[0] - 6
    f3 = x[0] * x[1] * x[2] - 6
    return np.array([f1, f2, f3])

def func_2__duas_equacoes(x):
    f1 = 3 * x[0]**2 - 2 * x[1]
    f2 = x[0] + x[1]**2 - 4
    return np.array([f1, f2])

def func_2__tres_equacoes(x):
    f1 = x[0]**2 + x[1] - 2
    f2 = x[1]**2 - x[0] - 3
    f3 = x[0] + x[1] + x[2] - 5
    return np.array([f1, f2, f3])

# JACOBIANOS

def jacobian_func1__duas_equacoes(x):
    return np.array([
        [2*x[0], 2*x[1]],
        [x[1], x[0]]
    ])

def jacobian_func1__tres_equacoes(x):
    return np.array([
        [1, 1, 1],
        [x[1] + x[2], x[0] + x[2], x[0] + x[1]],
        [x[1]*x[2], x[0]*x[2], x[0]*x[1]]
    ])

def jacobian_func2__duas_equacoes(x):
    return np.array([
        [6 * x[0], -2],
        [1, 2 * x[1]]
    ])

def jacobian_func2__tres_equacoes(x):
    return np.array([
        [2 * x[0], 1, 0],
        [-1, 2 * x[1], 0],
        [1, 1, 1]
    ])