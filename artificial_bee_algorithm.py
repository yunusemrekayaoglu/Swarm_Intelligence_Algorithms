import numpy as np
import random


def obj(x):
    return sum(x ** 2)


def fit(x):
    if x >= 0:
        return 1 / (x + 1)
    else:
        return 1 + abs(x)


def rulet(p) -> int:  # p is the probability array
    r = np.random.rand()
    c = np.cumsum(p)
    for i in range(len(c)):
        if r <= c[i]:
            return i


pop_size = 32

isci_ari = int(pop_size // 2)  # cant be float, so we use // instead of /
gozcu_ari = int(pop_size // 2)

sayac = np.zeros([isci_ari, 1])  # this array holds non-improvement counter for each bee
D = 2
alt_sinir = -5
ust_sinir = 5

X = np.random.rand(isci_ari, D) * (ust_sinir - alt_sinir) + alt_sinir

limit_degeri = 10
iter_no = 100

F = np.empty([isci_ari, 1], dtype=float)
fit = np.empty([isci_ari, 1], dtype=float)
v = X.copy()
prob = np.zeros([isci_ari, 1], dtype=float)

for i in range(isci_ari):
    F[i] = obj(X[i])
    if F[i] >= 0:
        fit[i] = 1 / (F[i] + 1)
    else:
        fit[i] = 1 + abs(F[i])

for i in range(iter_no):
    # isci ari aşaması
    for i in range(isci_ari):
        k = np.random.randint(0, isci_ari)
        while k == i:
            k = np.random.randint(0, isci_ari)

        j = np.random.randint(0, D)
        phi = random.uniform(-1, 1)
        v[i][j] = X[i][j] + phi * (X[i][j] - X[k][j])
        v[i] = np.clip(v[i], alt_sinir, ust_sinir)
        f = obj(v[i])
        if f < F[i]:  # fit olsa idi, büyüktür olma durumuna bakılacaktı
            X[i] = v[i].copy()
            F[i] = f
            sayac[i] = 0
            if F[i] >= 0:
                fit[i] = 1 / (F[i] + 1)
            else:
                fit[i] = 1 + abs(F[i])
        else:
            sayac[i] += 1

    # gozcu ari aşaması
    sum_fit = np.sum(fit)
    prob = fit / sum_fit

    for g in range(gozcu_ari):
        i = rulet(prob)
        k = np.random.randint(0, isci_ari)
        while k == i:
            k = np.random.randint(0, isci_ari)
        j = np.random.randint(0, D)
        phi = random.uniform(-1, 1)

        v[i][j] = X[i][j] + phi * (X[i][j] - X[k][j])
        v[i] = np.clip(v[i], alt_sinir, ust_sinir)
        f = obj(v[i])
        if f < F[i]:
            X[i] = v[i].copy()
            F[i] = f
            sayac[i] = 0
            if F[i] >= 0:
                fit[i] = 1 / (F[i] + 1)
            else:
                fit[i] = 1 + abs(F[i])
        else:
            sayac[i] += 1

    Gbest_X = X[np.argmin(F)]
    Gbest_f = obj(Gbest_X)

    # sayaç kontrolü
    # isci ari emeklilik aşaması # kaşif arı aşaması
    for i in range(isci_ari):
        if sayac[i] >= limit_degeri:
            X[i] = np.random.rand(D) * (ust_sinir - alt_sinir) + alt_sinir
            F[i] = obj(X[i])
            sayac[i] = 0
            if F[i] >= 0:
                fit[i] = 1 / (F[i] + 1)
            else:
                fit[i] = 1 + abs(F[i])

        if F[i] < Gbest_f:
            Gbest_X = X[i].copy()
            Gbest_f = F[i].copy()

    Gbest_X = X[np.argmin(F)]
    Gbest_f = obj(Gbest_X)

print(f"Minimum value: {np.min(F)}")
print(f"Minimum point: {X[np.argmin(F)]}")
