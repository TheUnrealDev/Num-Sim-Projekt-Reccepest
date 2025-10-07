from matplotlib import pyplot as plt
import numpy as np
import SEIRDV_monte_carlo as seirdv

num_samples = 100
INITIAL_SUS = 5
N = 1000  # Populationsstorlek
t_span = [0, 365] # Simuleringslängd i dagar
t_eval = np.arange(t_span[0], t_span[1], 1) # Tidssteg

alpha = 1/10  # Inkubationstid
beta = 0.3  # Antalet exponerade per tidsenhet
gamma = 1/7  # Andelen sjuka som tillfrisknar per tidsenhet
my = 0.01  # Död per tidsenhet
nu = 0.3  # Vaccinationstakt

values = {}
values["alpha"] = alpha
values["beta"] = beta
values["gamma"] = gamma
values["my"] = my
values["nu"] = nu

values["N"] = N
values["initial_sus"] = INITIAL_SUS
values["num_samples"] = num_samples
values["t_span"] = t_span
values["time_step"] = 1
seirdv_samples = seirdv.mc_simulate(values)

plt.plot(t_eval, seirdv_samples[:, 0], label="S", color="yellow")
plt.plot(t_eval, seirdv_samples[:, 1], label="E", color="orange")
plt.plot(t_eval, seirdv_samples[:, 2], label="I", color="red")
plt.plot(t_eval, seirdv_samples[:, 3], label="R", color="lightgreen")
plt.plot(t_eval, seirdv_samples[:, 4], label="D", color="black")
plt.plot(t_eval, seirdv_samples[:, 5], label="V", color="lightblue")

plt.legend()
plt.show()

