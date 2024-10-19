import numpy as np


def obj(x):
    return (x[0] - 5) ** 2 + (x[1]- 2) ** 2


def grey_wolf(run = 30, N = 20, lb = -10, ub = 10, T = 100, D = 2):
    run_best = np.empty([run, 1])  #?
    for run in range(run):
        np.random.seed(run)
        X = np.random.rand(N, D) * (ub - lb) + lb

        ## create function's params
        f = np.empty([N, 1])
        for i in range(N):
            f[i] = obj(X[i])

        sorted = np.argsort(f, axis = 0)
        X_alpha = X[sorted[0]].reshape(-1)
        X_beta = X[sorted[1]].reshape(-1)
        X_delta = X[sorted[2]].reshape(-1)

        f_alpha = f[sorted[0]].reshape(-1)
        f_beta = f[sorted[1]].reshape(-1)
        f_delta = f[sorted[2]].reshape(-1)

        # find a params
        for t in range(T):
            a = 2 - 2 * (t / T)

            for i in range(N):
                for j in range(D):





                    # we need to upgrade r1 and r2 all the time
                    r1 = np.random.rand()
                    r2 = np.random.rand()
                    # for alpha wolf
                    A_alpha = 2 * a * r1 - a
                    C_alpha = 2 * r2

                    D_alpha = np.abs(C_alpha * X_alpha[j] - X[i][j]) #why alpha[j]?

                    P_alpha = X_alpha[j] - A_alpha * D_alpha

                    # for beta wolf
                    r1 = np.random.rand()
                    r2 = np.random.rand()

                    A_beta = 2 * a * r1 - a
                    C_beta = 2 * r2
                    D_beta = np.abs(C_beta * X_beta[j] - X[i][j])
                    P_beta = X_beta[j] - A_beta * D_beta


                    # for delta wolf
                    r1 = np.random.rand()
                    r2 = np.random.rand()

                    A_delta = 2 * a * r1 - a
                    C_delta = 2 * r2
                    D_delta = np.abs(C_delta * X_delta[j] - X[i][j])
                    P_delta = X_delta[j] - A_delta * D_delta


                    # need to find new X1's location
                    X[i][j] = (P_alpha + P_beta + P_delta) / 3


            #now need to update old location to new location
            for i in range(N):
                X[i] = np.clip(X[i], lb, ub)
                f[i] = obj(X[i])

                if f[i] <= f_alpha:
                    X_alpha = X[i].copy()
                    f_alpha = f[i].copy()

                if f[i] <= f_beta and f[i] > f_alpha:
                    X_beta = X[i].copy()
                    f_beta = f[i].copy()

                if f[i] <= f_delta and f[i] > f_alpha and f[i] > f_beta:
                    X_delta = X[i].copy()
                    f_delta = f[i].copy()
            print("X_alpha: ", X_alpha, "Best: ", obj(X_alpha))
            run_best[run] = obj(X_alpha).copy()
        print("Ortalama: ", np.mean(run_best))
        print("Standart Sapma: ", np.std(run_best))  # standart sapma küçük yani güzel bir sonuç


grey_wolf()