import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
from gillespie import SSA
from time import time
import math
from os import system

INITIAL_SUS = 5
N = 1000
beta = 0.3
gamma = 1/7

sus0 = N - INITIAL_SUS
inf0 = INITIAL_SUS
rec0 = 0

x0 = [sus0, inf0, rec0]
t_span = [0, 120]
coeff = [beta, gamma]

num_samples = 100
t_eval = np.arange(t_span[0], t_span[1], 1)
samples = np.zeros([len(t_eval), 3])
sol_x = []

# Returnerar stokiometritabell där rad representerar "händelser" och kolumn representerar "komponenter"

def stoch():
    return np.array([
    [-1, 1, 0],    # Inf
    [0, -1, 1]     # Rec
])

def prop(y, coeff):
    sus, inf, res = y
    beta, gamma = coeff
    
    prob_inf = beta * sus * inf / N
    prob_res = gamma * inf
    
    return np.array([prob_inf, prob_res])

prev_percentage = -1
start_time = time()

for i in range(num_samples):
    percentage = math.floor((i / num_samples) * 100) + 1
    if percentage > prev_percentage:
        prev_percentage = percentage
        system("cls")
        print(f"Percentage completed: {percentage}%")
        

    sol_x, sol_y = SSA(prop, stoch, x0.copy(), t_span, coeff.copy())

    S = np.interp(t_eval, sol_x, sol_y[:, 0])
    I = np.interp(t_eval, sol_x, sol_y[:, 1])
    R = np.interp(t_eval, sol_x, sol_y[:, 2])

    samples[:, 0] += S
    samples[:, 1] += I
    samples[:, 2] += R

end_time = time()
print(f"Duration: {math.floor((end_time - start_time)*100) / 100} s")
print("Uhm the calculation is finished 🤓☝️")

samples /= num_samples

plt.plot(t_eval, samples[:, 0], label="S", color="yellow")
plt.plot(t_eval, samples[:, 1], label="I", color = "red")
plt.plot(t_eval, samples[:, 2], label="R", color = "lightgreen")

plt.legend()
plt.show()


