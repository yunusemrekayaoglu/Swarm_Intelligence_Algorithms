import numpy as np

np.random.seed(1)


def obj(X):
    return sum(X**2)


def pso(type = "min", lb = -5.12, ub = 5.12, D = 2, N = 30, c1 = 2, c2 = 2, T = 100, r1 = np.random.rand(), r2 = np.random.rand(), w = 0.8):
    X = np.random.rand(N, D)  * (ub - lb) + lb # N*D matrix
    F = np.empty([N], dtype=float)
    for i in range(N):
        F[i] = obj(X[i])

    v = np.zeros([N, D])
    pbest = X.copy()
    pbest_obj = F.copy()

    gbest = X[np.argmin(F)]
    gbest_obj = np.min(F)

    for t in range(T):
        v = w * v + c1* r1 * (pbest - X) + c2 * r2 * (gbest - X)
        X = X + v
        X = np.clip(X, lb, ub)
        for i in range(N):
            F[i] = obj(X[i])
            if type == "min":
                if F[i] < pbest_obj[i]:
                    pbest_obj[i] = F[i].copy()
                    pbest[i] = X[i].copy()
                if F[i] < gbest_obj:
                    gbest_obj = F[i].copy()
                    gbest = X[i].copy()
            elif type == "max":
                if F[i] > pbest_obj[i]:
                    pbest_obj[i] = F[i].copy()
                    pbest[i] = X[i].copy()
                if F[i] > gbest_obj:
                    gbest_obj = F[i].copy()
                    gbest = X[i].copy()
            else:
                return "give me your problems correct"

    return gbest, gbest_obj


pso_ = pso("min")
print(pso_)