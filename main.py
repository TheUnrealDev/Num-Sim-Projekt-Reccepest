import math
from matplotlib import pyplot as plt
import numpy as np
import SIR_monte_carlo as sir
import SEIRD_monte_carlo as seir
import SEIRD_monte_carlo as seird
import SEIRDV_monte_carlo as seirdv
from os import system
from time import time

num_samples = 10 # Antalet körningar som körs med varje metod.
INITIAL_INF = 5 # Det initiala antalet infekterade.
N = 1000  # Populationsstorlek
t_span = [0, 250] # Simuleringslängd
t_eval = np.arange(t_span[0], t_span[1], 1) # Tidssteg

alpha = 1/10  # Inkubationstid
beta = 0.3 # Smittspridningstakt
gamma = 1/7  # Tillfriskningstakt
my = 0.01  # Dödstakt
nu = 0.3  # Vaccinationstakt

values = {} # Initialiserar en dictionary som innehåller alla värden, 
# denna skickas senare till varje metod så att alla använder samma värden.

values["alpha"] = alpha
values["beta"] = beta
values["gamma"] = gamma
values["my"] = my
values["nu"] = nu

values["N"] = N
values["initial_inf"] = INITIAL_INF
values["num_samples"] = num_samples
values["t_span"] = t_span
values["time_step"] = 1

start_time = time()

# Kör Monte Carlo simulering för respektive modeller.
sir_samples = sir.mc_simulate(values, should_print=True)
print("SIR Complete!")
seir_samples = seir.mc_simulate(values, should_print=True)
print("SEIR Complete!")
seird_samples = seird.mc_simulate(values, should_print=True)
print("SEIRD Complete!")
seirdv_samples = seirdv.mc_simulate(values, should_print=True)
print("SEIRDV Complete!")

duration = time() - start_time

# Plottar resultaten
fig, ax = plt.subplots(2, 2)
fig.suptitle("Epidemimodellering")

ax1 = ax[0, 0]
ax1.set_title("SIR")
ax1.plot(t_eval, sir_samples[:, 0], label="S", color="yellow")
ax1.plot(t_eval, sir_samples[:, 1], label="I", color="red")
ax1.plot(t_eval, sir_samples[:, 2], label="R", color="lightgreen")
ax1.legend()

ax2 = ax[0, 1]
ax2.set_title("SEIR")
ax2.plot(t_eval, seir_samples[:, 0], label="S", color="yellow")
ax2.plot(t_eval, seir_samples[:, 1], label="E", color="orange")
ax2.plot(t_eval, seir_samples[:, 2], label="I", color="red")
ax2.plot(t_eval, seir_samples[:, 3], label="R", color="lightgreen")
ax2.legend()

ax3 = ax[1, 0]
ax3.set_title("SEIRD")
ax3.plot(t_eval, seird_samples[:, 0], label="S", color="yellow")
ax3.plot(t_eval, seird_samples[:, 1], label="E", color="orange")
ax3.plot(t_eval, seird_samples[:, 2], label="I", color="red")
ax3.plot(t_eval, seird_samples[:, 3], label="R", color="lightgreen")
ax3.plot(t_eval, seird_samples[:, 4], label="D", color="black")
ax3.legend()

ax4 = ax[1, 1]
ax4.set_title("SEIRDV")
ax4.plot(t_eval, seirdv_samples[:, 0], label="S", color="yellow")
ax4.plot(t_eval, seirdv_samples[:, 1], label="E", color="orange")
ax4.plot(t_eval, seirdv_samples[:, 2], label="I", color="red")
ax4.plot(t_eval, seirdv_samples[:, 3], label="R", color="lightgreen")
ax4.plot(t_eval, seirdv_samples[:, 4], label="D", color="black")
ax4.plot(t_eval, seirdv_samples[:, 5], label="V", color="lightblue")
ax4.legend()

fig.supxlabel(f"α={alpha} β={beta} γ={math.floor(gamma * 100) / 100} μ={my} ν={nu} pop={N} start_inf={INITIAL_INF} time_span=[{t_span[0]}, {t_span[1]}] num_samples={num_samples}")
system("cls")
print(f"Percentage completed: 100%")
print(f"Duration: {(math.floor(duration)*100) / 100} s")

plt.show()

