import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt

INITIAL_INF = 5
N = 1000
beta = 0.3
gamma = 1/7

t_span = [0, 120]
t_eval = np.arange(t_span[0], t_span[1], 0.01)
print(t_eval)
y0 = [N - INITIAL_INF, INITIAL_INF, 0]

def ODE_rhs(t, y):
    sus, inf, res = y
    
    new_sus = -1 * beta * (inf / N) * sus
    new_inf = beta * (inf / N) * sus - gamma * inf
    new_res = gamma * inf
    
    return [new_sus, new_inf, new_res]

result = sp.solve_ivp(ODE_rhs, t_span, y0, t_eval=t_eval)
print(result)
x = result.t
plt.plot(x, result.y[0], label="Sus", color="red")
plt.plot(x, result.y[1], label="Inf", color="blue")
plt.plot(x, result.y[2], label="Res", color="green")

plt.legend()
plt.show()