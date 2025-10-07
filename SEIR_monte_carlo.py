import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
from gillespie import SSA
from time import time
import math
from os import system

# Returnerar stokiometritabell där rad representerar "händelser" och kolumn representerar "komponenter"
def stoch():
    return np.array([
    [-1, 1, 0, 0], # Exp
    [0, -1, 1, 0], # Inf
    [0, 0, -1, 1], # Rec
])

def prop(y, coeff):
    sus, exp, inf, res = y
    alpha, beta, gamma, N = coeff
    
    prob_exp = beta * sus * inf / N
    prob_inf = alpha * exp
    prob_res = gamma * inf
    
    return np.array([prob_exp, prob_inf, prob_res])

prev_percentage = -1
start_time = time()

def mc_simulate(values, should_print=False):
    N = values["N"]
    initial_inf = values["initial_inf"]
    alpha = values["alpha"]  # Inkubationstid
    beta = values["beta"]  # Antalet exponerade per tidsenhet
    gamma = values["gamma"]  # Andelen sjuka som tillfrisknar per tidsenhet
    num_samples = values["num_samples"]
    t_span = values["t_span"]
    time_step = values["time_step"]
    t_eval = np.arange(t_span[0], t_span[1], time_step)

    sus0 = N - initial_inf
    exp0 = 0
    inf0 = initial_inf
    res0 = 0

    coeff = [alpha, beta, gamma, N] # VARIERAR FRÅN FIL TILL FIL
    x0 = [sus0, exp0, inf0, res0]

    samples = np.zeros([len(t_eval), len(x0)])
    prev_percentage = -1
    start_time = time()

    for i in range(num_samples):
        percentage = math.floor((i / num_samples) * 100) + 1
        if should_print and percentage > prev_percentage:
            prev_percentage = percentage
            system("cls")
            print(f"Percentage completed: {percentage}%")

        sol_x, sol_y = SSA(prop, stoch, x0.copy(), t_span, coeff.copy())

        S = np.interp(t_eval, sol_x, sol_y[:, 0])
        E = np.interp(t_eval, sol_x, sol_y[:, 1])
        I = np.interp(t_eval, sol_x, sol_y[:, 2])
        R = np.interp(t_eval, sol_x, sol_y[:, 3])

        samples[:, 0] += S
        samples[:, 1] += E
        samples[:, 2] += I
        samples[:, 3] += R  

    end_time = time()
    if should_print:
        print(f"Duration: {math.floor((end_time - start_time)*100) / 100} s")
        print("Uhm the calculation is finished 🤓☝️")

    samples /= num_samples

    return samples

