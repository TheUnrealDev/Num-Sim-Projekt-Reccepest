import numpy as np
import scipy.integrate as sp
import matplotlib.pyplot as plt
from gillespie import SSA

INITIAL_SUS = 5
N = 1000
beta = 0.3
gamma = 1/7


# HELA DEN HÄR FILEN ÄR GALEN WORK IN PROGRESS
# (YOINK)
def prop(y, coeff):
    sus, inf, res = y
    
    new_sus = -1 * beta * (inf / N) * sus
    new_inf = beta * (inf / N) * sus - gamma * inf
    new_res = gamma * inf
    
    return [new_sus, new_inf, new_res]

stoch = []
x0 = []
t_span = [0, 120]
coeff = []
sol_x, sol_y = SSA(prop, stoch, x0, t_span, coeff)
