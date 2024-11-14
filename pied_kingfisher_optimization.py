import numpy as np

def obj(X):
    return sum(X ** 2)


def kingfisher_optimization(N = 20,
                            Tmax = 500,
                            Dim = 2,
                            ub = 10,
                            lb = -10,
                            BF = 8):
    X = np.random.rand(N, Dim) * (ub - lb) + lb
    f = np.empty(N)
    for i in range(N):
        f[i] = obj(X[i])
    idx = np.argmin(f)
    Xbest = X[idx]
    fbest = f[idx]

    Xnew = np.empty([N, Dim])
    Fnew = np.empty(N)

    t = 1
    while t < Tmax:
        o = np.exp((-t / Tmax) ** 2)
        PE = 0.5 - (0.5 - 0) * (t / Tmax)
        for i in range(N):
            if np.random.rand() < 0.8:
                alpha = 2 * np.random.randn(Dim)
                j = np.random.randint(0, N)
                while j == i:
                    j = np.random.randint(0, N)
                if np.random.rand() < 0.5:
                    CA = 2 * np.pi * np.random.rand()
                    T = np.exp(1) - np.exp((((t - 1) / Tmax) ** (1 / BF)) ) * np.cos(CA)
                    Xnew[i] = X[i] + alpha * T * (X[j] - X[i])
                else:
                    BR = np.random.rand() * f[j] / f[i]
                    T = BR * (t / Tmax) ** (1 / BF)
                    Xnew[i] = X[i] + alpha * T * (X[j] - X[i])
            else:
                alpha = 2 * np.random.randn(Dim)
                HA = np.random.rand() * f[i] / fbest
                b = X[i] + o ** 2 * np.random.rand() * Xbest
                Xnew[i] = X[i] + HA * o * alpha * (b - Xbest)
        for i in range(N):
            Xnew[i] = np.clip(Xnew[i], lb, ub)
            Fnew[i] = obj(Xnew[i])
            if Fnew[i] < f[i]:
                f[i] = Fnew[i]
                X[i] = Xnew[i]
            if f[i] < fbest:
                fbest = f[i].copy()
                Xbest = X[i].copy()

        for i in range(N):
            if np.random.rand() > (1 - PE):
                m = np.random.randint(0, N)
                n = np.random.randint(0, N)
                alpha = 2 * np.random.randn(Dim)

                Xnew[i] = X[m] + o * alpha * abs(X[i] - X[n])
            else:
                Xnew[i] = X[i].copy()


        for i in range(N):
            Xnew[i] = np.clip(Xnew[i], lb, ub)
            Fnew[i] = obj(Xnew[i])
            if Fnew[i] < f[i]:
                f[i] = Fnew[i]
                X[i] = Xnew[i]
            if f[i] < fbest:
                fbest = f[i].copy()
                Xbest = X[i].copy()

        t += 1
    print(Xbest, fbest)



kingfisher_optimization()