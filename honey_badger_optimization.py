import numpy as np


def obj(X):
    return sum(X ** 2)

def honey_badger_optimization(N = 20,
                              beta = 6,
                              C = 2,
                              T = 500,
                              Dim = 2,
                              ub = 10,
                              lb = -10):
    X = np.random.rand(N, Dim) * (ub - lb) + lb
    F = np.empty(N)
    for i in range(N):
        F[i] = obj(X[i])
    idx = np.argmin(F)
    X_prey = X[idx]
    F_prey = F[idx]
    Xnew = np.empty([N, Dim])
    Fnew = np.empty(N)
    eps = np.finfo(float).eps


    t = 0
    while t < T:

        alpha = C * np.exp(-t / T)
        for i in range(N):
            if np.random.rand() < 0.5:
                f = 1
            else:
                f = -1
            if i == N - 1:
                S = (X[i] - X[0]) ** 2
            else:
                S =(X[i] - X[i + 1] + eps) ** 2
            d = X_prey - X[i] + eps
            I = np.random.rand() * S / (4 * np.pi * d ** 2)
            if np.random.rand() < 0.5:
                #kazma aşaması
                r1 = np.random.rand()
                r2 = np.random.rand()
                r3 = np.random.rand()
                Xnew[i] = X_prey + f * beta * I * X_prey + f * \
                          alpha * r1 * d * abs(np.cos(2 * np.pi * r2) * (1 - np.cos(2 * np.pi * r3)))
            else:
                #bal aşaması
                r4 = np.random.rand()
                Xnew[i] = X_prey + f * r4 * alpha * d
        for i in range(N):
            Xnew[i] = np.clip(Xnew[i], lb, ub)
            Fnew[i] = obj(Xnew[i])
            if Fnew[i] < F[i]:
                X[i] = Xnew[i].copy()
                F[i] = Fnew[i].copy()
        for i in range(N):
            if F[i] < F_prey:
                F_prey = F[i].copy()
                X_prey = X[i].copy()
        t += 1
    print(F_prey)
    print("-" * 50)
    print(X_prey)
    print("-" * 50)


honey_badger_optimization()