import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
from gillespie import SSA

INITIAL_SUS = 5
N = 1000
beta = 0.3
gamma = 1/7

sus0 = N - INITIAL_SUS
inf0 = INITIAL_SUS
rec0 = 0

x0 = [sus0, inf0, rec0]
t_span = [0, 120]
coeff = []

# Retunerar stokiometritabell där rad representerar "händelser" och kolumn representerar "komponenter"

def stoch():
    return np.array([
    [-1, +1, 0],    # Inf
    [0, -1, +1]     # Rec
])

# HELA DEN HÄR FILEN ÄR GALEN WORK IN PROGRESS
# (YOINK)
def prop(y, coeff):
    sus, inf, res = y
    
    new_inf = beta * sus * inf / N
    new_res = gamma * inf
    
    return np.array([new_inf, new_res])


sol_x, sol_y = SSA(prop, stoch, x0, t_span, coeff)

plt.plot(sol_x, sol_y[0])
plt.plot(sol_x, sol_y[1])
plt.plot(sol_x, sol_y[2])
plt.show()
