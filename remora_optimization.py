import numpy as np
import math
np.random.seed(12)
#def obj(X):
#   return sum(X ** 2)

def obj(X):
    t = (1 / 4000) * sum(X ** 2) + 1
    c = 1
    for j  in range(len(X)):
        c = np.cos(X[j] / np.sqrt(j + 1))
    return (t - c)

def remore_opt(N = 50, Dim = 2, lb = -100, ub = 100, C = 0.1, T = 200):
    R = lb + (ub - lb) * np.random.rand(N, Dim)
    t = 0
    fit = np.empty(N)
    fitBest = np.inf
    temp = R.copy()
    while t < T:
        for i in range(N):
            R[i] = np.clip(R[i], lb, ub)
            fit[i] = obj(R[i])
            if fit[i] < fitBest:
                fitBest = fit[i].copy()
                Rbest = R[i].copy()
        if t == 0:
            Rpre = R.copy()
        else:
            Rpre = temp.copy()
            temp = R.copy()

        for i in range(N):
            Ratt = R[i] + (R[i] - Rpre[i]) * np.random.randn()
            fitAtt = obj(Ratt)
            if fit[i] < fitAtt:
                H = np.random.randint(0, 2)
                if H == 0:
                    D = abs(Rbest - R[i])
                    a = - (1 + t / T)
                    alpha = np.random.rand() * (a - 1) + 1
                    R[i] = D * np.exp(a) * np.cos(2 * np.pi * alpha) + R[i]
                else:
                    Rrand = R[np.random.randint(0, N)].copy()
                    R[i] = Rbest - (np.random.rand() * ((Rbest + Rrand) / 2) - Rrand)
            else:
                V = 2 * (1 - t / T)
                B = 2 * V * np.random.rand() - V
                A = B * (R[i] - C * Rbest)
                R[i] = R[i] + A
        t += 1
    print(fitBest)


remore_opt(Dim = 50,
           lb = -600,
           ub = 600)