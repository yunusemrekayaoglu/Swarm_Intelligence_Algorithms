import numpy as np
#np.random.seed(42)
import matplotlib.pyplot as plt
def obj(X):
    return sum(X ** 2)


# Whale Optimization Algorithm
def whale_optimization(lb=-5.12, ub=5.12, dim=2, N=30, T=100):
    # Initialize search agents
    X = np.random.rand(N, dim) * (ub - lb) + lb
    F = np.zeros(N)

    # Calculate initial fitness values
    for i in range(N):
        F[i] = obj(X[i])
    fval = []

    idx = np.argsort(F)  # Sort the agents by fitness
    Xbest = X[idx[0]]  # Best solution
    Fbest = F[idx[0]]  # Best fitness value
    fval.append(Fbest)
    t = 0  # Iteration counter

    while t <= T:
        for i in range(N):
            a = 2 - 2 * t / T
            r1 = np.random.rand()
            r2 = np.random.rand()
            A = 2 * a * r1 - a
            C = 2 * r2
            a1 = -1 + (-1) * t / T
            r3 = np.random.rand()
            l = (a1 - 1) * r3 + 1
            b = 1
            p = np.random.rand()

            if p < 0.5:
                if abs(A) < 1:
                    D = C * Xbest - X[i]
                    X[i] = Xbest - A * D
                else:
                    rand = np.random.randint(0, N)
                    D_other = abs(C * X[rand] - X[i])
                    X[i] = X[rand] - A * D_other
            else:
                D = abs(Xbest - X[i])
                X[i] = D * np.exp(b * l) * np.cos(2 * np.pi * l) + Xbest

        # Apply boundary constraints
        X = np.clip(X, lb, ub)

        # Recalculate fitness and update the best solution
        for i in range(N):
            F[i] = obj(X[i])
            if Fbest > F[i]:
                Fbest = F[i]
                Xbest = X[i].copy()

        t = t + 1
        fval.append(Fbest)
    plt.plot(fval)
    plt.show()
    return Xbest, Fbest, fval


# Run the algorithm
a = whale_optimization()
print(a)
