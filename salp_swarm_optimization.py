import numpy as np

def obj(X):
    return sum(X**2)

#N popülasyon sayısı
#D boyut sayısı
def salp_optimization(N = 20, T = 100, lb = -5, ub = 5, D = 2):
    X = np.random.rand(N, D) * (ub - lb) + lb
    t = 0
    fit = np.empty(N)
    fitBest = np.inf
    while t < T + 1:
        for i in range(N):
            X[i] = np.clip(X[i], lb, ub)
            fit[i] = obj(X[i])
            if fit[i] < fitBest:
                fitBest = fit[i].copy()
                F = X[i].copy()

        c1 = 2 * np.exp((-4 * t / T) ** 2)

        for i in range(N):
            for j in range(D):
                if i <= N / 2:
                    c2 = np.random.rand()
                    c3 = np.random.rand()
                    if c3 >= 0.5:
                        X[i][j] = F[j] + c1 * ((ub - lb) * c2 + lb)
                    else:
                        X[i][j] = F[j] - c1 * ((ub - lb) * c2 + lb)
                else:
                    X[i][j] = (X[i][j] + X[i - 1][j]) / 2

            t = t + 1

    print(fitBest, F)



salp_optimization()