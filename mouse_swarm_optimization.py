import numpy as np

def obj(X):
    return sum(X ** 2)



def mouse_swarm(N = 30, T = 100, lb = -5, ub = 5, D = 2):
    P = np.random.rand(N, D) * (ub - lb) + lb
    fit = np.empty(N)
    t = 0
    f_val = []
    fitbest = np.inf
    while t < T:
        for i in range(N):
            P[i] = np.clip(P[i], lb, ub)
            fit[i] = obj(P[i])
            if fit[i] < fitbest:
                fitbest = fit[i].copy()
                Pr = P[i].copy()
        R = 4 * np.random.rand() + 1
        A = R - t * R / T

        for i in range(N):
            for j in range(D):
                C = 2 * np.random.rand()
                Pd = A * P[i][j] + C * (Pr[j] - P[i][j])
                P[i][j] =  Pr[j] - Pd
        t += 1
    print(fitbest, Pr)



mouse_swarm()