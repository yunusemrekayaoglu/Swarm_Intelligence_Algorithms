import numpy as np
import math

def obj_1(X):
    """
    D = 10
    lb = -10
    ub = 10
    Fmin --> 0
    """
    sum_part = sum(abs(X))
    prod_part = np.prod(abs(X))
    return sum_part + prod_part

def obj_2(X):
    """
    D = 10
    lb = -30
    ub = 30
    Fmin --> 0
    """
    D = len(X)
    sum_part = 0
    for i in range(D - 1):
        sum_part += 100 * (X[i + 1] - X[i] ** 2)  ** 2 + (X[i] - 1) ** 2
    return sum_part

def obj_3(X):
    """
    D = 10
    lb = -100
    ub = 100
    Fmin --> 0
    """

    return sum((X + 0.5) ** 2)

def obj_4(X):
    """
    D = 10
    lb = -1.28
    ub = 1.28
    """
    D = len(X)
    sum_part = sum([(i + 1) * X[i] ** 4 for i in range(D)])
    random_part = np.random.random()

    return sum_part + random_part

def obj_5(X):
    """
    D = 10
    lb = -500
    ub = 500
    Fmin --> -418.9839 * D
    """

    return sum(-X * np.sin(np.sqrt(np.abs(X))))

def obj_6(X):
    """
    D = 10
    lb = -5.12
    ub = 5.12
    Fmin --> 0
    """

    return sum(X ** 2 - 10 * np.cos(2 * np.pi * X) + 10)

def obj_7(X):
    """
    D = 10
    lb = -32
    ub = 32
    Fmin --> 0
    """
    D = len(X)
    term1 = -20 * np.exp(-0.2 * np.sqrt(np.mean(X ** 2)))
    term2 = -np.exp(np.mean(np.cos(2 * np.pi * X)))

    return term1 + term2 + 20 + np.e

def obj_8(X):
    """
    D = 2
    lb = -5
    ub = 5
    Fmin --> -1.0316
    """
    X1 = X[0]
    X2 = X[1]

    return 4 * X1 ** 2 - 2.1 * X1 ** 4 + (1 / 3) * X1 ** 6 + X1 * X2

def obj_9(X):
    """
    D = 2
    lb = -5
    ub = 5
    Fmin --> 0.398
    """
    X1 = X[0]
    X2 = X[1]
    term1 = ( X2 - ( 5.1 / ( 4 * np.pi ** 2)) * X1 ** 2 + (5 / np.pi) * X1 - 6) ** 2
    term2 = 10 * (1 - 1 / (8 * np.pi)) * np.cos(X1)

    return term1 + term2 + 10

def obj_10(X):
    """
    D = 2
    lb = -2
    ub = 2
    Fmin --> 3
    """
    X1 = X[0]
    X2 = X[1]
    term1 = (X1 + X2 + 1) ** 2
    term2 = 19 - 14 ** X1 + 3 * X1 ** 2 - 14 * X2 + 6 * X1 * X2 + 3 * X2 ** 2

    term3 = (2 * X1 - 3 * X2) ** 2
    term4 =18 - 32 * X1 + 12 * X1 ** 2 + 48 * X2 - 36 * X1 * X2 + 27 * X2 ** 2

    return (1 + term1 + term2) * (30 + term3 + term4)

