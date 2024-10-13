import numpy as np



def obj(X):
    return sum(X**2)

"""
a -> 
T -> iteration count
n -> population size
phi -> tilki gözlem açısı
theta -> hava durumu
"""

def rfo(a = np.random.uniform(0, 0.2), b = np.random.uniform(0, 0.2), T = 100, n = 10, phi = np.random.uniform(0, 1), theta_0 = np.random.uniform(0, (2 * np.pi))):
    X = np.random.uniform(a, b, n)
    t = 0
    while t < T:

    return X




rfo_ = rfo()

print(rfo_)