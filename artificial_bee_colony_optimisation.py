import numpy as np
import random

def objective_function(x):
    """Hesaplanan nesne fonksiyonu."""
    return sum(x ** 2)

def fitness_function(f):
    """Fitness değerini hesaplar."""
    if f >= 0:
        return 1 / (f + 1)
    else:
        return 1 + abs(f)

def roulette_wheel_selection(probabilities):
    """Roulette wheel selection yöntemi ile bir index döndürür."""
    r = np.random.rand()
    cumulative_prob = np.cumsum(probabilities)
    for i in range(len(cumulative_prob)):
        if r <= cumulative_prob[i]:
            return i

def abc_algorithm(pop_size=32, dimensions=2, lower_bound=-5, upper_bound=5, iterations=100, limit_value=10):
    """ABC optimizasyon algoritmasını uygular."""
    worker_bees = pop_size // 2
    scout_bees = pop_size // 2

    X = np.random.rand(worker_bees, dimensions) * (upper_bound - lower_bound) + lower_bound
    F = np.zeros(worker_bees)
    fitness_values = np.zeros(worker_bees)
    non_improvement_counter = np.zeros(worker_bees)

    for i in range(worker_bees):
        F[i] = objective_function(X[i])
        fitness_values[i] = fitness_function(F[i])

    Gbest_X = X[np.argmin(F)]
    Gbest_f = np.min(F)

    # Ana döngü
    for iter in range(iterations):
        # Emekçi arılar aşaması
        for i in range(worker_bees):
            k = np.random.randint(0, worker_bees)
            while k == i:
                k = np.random.randint(0, worker_bees)

            j = np.random.randint(0, dimensions)
            phi = random.uniform(-1, 1)
            v = X[i].copy()
            v[j] = X[i][j] + phi * (X[i][j] - X[k][j])
            v = np.clip(v, lower_bound, upper_bound)

            f_v = objective_function(v)
            if f_v < F[i]:
                X[i] = v
                F[i] = f_v
                fitness_values[i] = fitness_function(F[i])
                non_improvement_counter[i] = 0
            else:
                non_improvement_counter[i] += 1

        # Gözcü arılar aşaması
        total_fitness = np.sum(fitness_values)
        probabilities = fitness_values / total_fitness if total_fitness > 0 else np.ones(worker_bees) / worker_bees

        for g in range(scout_bees):
            i = roulette_wheel_selection(probabilities)
            k = np.random.randint(0, worker_bees)
            while k == i:
                k = np.random.randint(0, worker_bees)
            j = np.random.randint(0, dimensions)
            phi = random.uniform(-1, 1)

            v = X[i].copy()
            v[j] = X[i][j] + phi * (X[i][j] - X[k][j])
            v = np.clip(v, lower_bound, upper_bound)

            f_v = objective_function(v)
            if f_v < F[i]:
                X[i] = v
                F[i] = f_v
                fitness_values[i] = fitness_function(F[i])
                non_improvement_counter[i] = 0

        # En iyi çözümü güncelle
        Gbest_X = X[np.argmin(F)]
        Gbest_f = np.min(F)

        # Emekçi arı emeklilik aşaması
        for i in range(worker_bees):
            if non_improvement_counter[i] >= limit_value:
                X[i] = np.random.rand(dimensions) * (upper_bound - lower_bound) + lower_bound
                F[i] = objective_function(X[i])
                fitness_values[i] = fitness_function(F[i])
                non_improvement_counter[i] = 0

        # En iyi çözümü tekrar güncelle
        Gbest_X = X[np.argmin(F)]
        Gbest_f = np.min(F)

    return Gbest_f, Gbest_X

if __name__ == '__main__':
    best_fitness, best_position = abc_algorithm()
    print(f"Minimum Değer: {best_fitness}")
    print(f"Minimum Nokta: {best_position}")
