import numpy as np
import matplotlib.pyplot as plt
from gillespie import SSA
from time import time
import math
from os import system

INITIAL_SUS = 5
N = 1000 # Populationsstorlek
alpha = 1/10 # Inkubationstid
beta = 0.3 # Antalet exponerade per tidsenhet
gamma = 1/7 # Andelen sjuka som tillfrisknar per tidsenhet
my = 0.01 # Död per tidsenhet

sus0 = N - INITIAL_SUS
exp0 = 0
inf0 = INITIAL_SUS
res0 = 0
ded0 = 0

x0 = [sus0, exp0, inf0, res0, ded0]
t_span = [0, 365]
coeff = [alpha, beta, gamma, my]

num_samples = 100
t_eval = np.arange(t_span[0], t_span[1], 1)
samples = np.zeros([len(t_eval), len(x0)])

# Returnerar stokiometritabell där rad representerar "händelser" och kolumn representerar "komponenter"


def stoch():
    return np.array([
        [-1, 1, 0, 0, 0],  # Exp
        [0, -1, 1, 0, 0],  # Inf
        [0, 0, -1, 1, 0],  # Rec
        [0, 0, -1, 0, 1],  #Ded
    ])


def prop(y, coeff):
    sus, exp, inf, res, ded = y
    alpha, beta, gamma, my = coeff

    prob_exp = beta * sus * inf / N
    prob_inf = alpha * exp
    prob_res = gamma * inf
    prob_ded = my * inf

    return np.array([prob_exp, prob_inf, prob_res, prob_ded])


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
    E = np.interp(t_eval, sol_x, sol_y[:, 1])
    I = np.interp(t_eval, sol_x, sol_y[:, 2])
    R = np.interp(t_eval, sol_x, sol_y[:, 3])
    D = np.interp(t_eval, sol_x, sol_y[:, 4])

    samples[:, 0] += S
    samples[:, 1] += E
    samples[:, 2] += I
    samples[:, 3] += R
    samples[:, 4] += D

end_time = time()
print(f"Duration: {math.floor((end_time - start_time)*100) / 100} s")
print("Uhm the calculation is finished 🤓☝️")

samples /= num_samples

plt.plot(t_eval, samples[:, 0], label="S", color="yellow")
plt.plot(t_eval, samples[:, 1], label="E", color="orange")
plt.plot(t_eval, samples[:, 2], label="I", color="red")
plt.plot(t_eval, samples[:, 3], label="R", color="lightgreen")
plt.plot(t_eval, samples[:, 4], label="D", color="black")

plt.legend()
plt.show()
