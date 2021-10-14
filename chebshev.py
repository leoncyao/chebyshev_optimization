
import numpy as np
import gurobipy as gp
from gurobipy import GRB
from gurobipy import quicksum
import json

import matplotlib.pyplot as plt

verbose = False

def optimize_quadratic():
    model = gp.Model("chebyshev")
    model.params.LogToConsole = 0
    model.params.NonConvex = 2
    
    a = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="a")
    a_pow_2 = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="a_pow_2")
    a_inv = model.addVar(lb=-100, ub = 100, vtype = GRB.CONTINUOUS, name = "a_inv")
    a_inv_pow_2 = model.addVar(lb=-100, ub = 100, vtype = GRB.CONTINUOUS, name = "a_inv_pow_2")

    b = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="b")
    b_pow_2 = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="b_pow_2")
    b_pow_3 = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="b_pow_3")
    b_pow_4 = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="b_pow_4")
    
    c = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="c")
    c_pow_2 = model.addVar(lb=-100, ub=100, vtype=GRB.INTEGER, name="c_pow_2")
    c_over_a = model.addVar(lb=-100, ub=100, vtype=GRB.CONTINUOUS, name="c_over_a")

    model.addConstr(a * a_inv == 1, "a_inv_constr")
    model.addConstr(a * a == a_pow_2, "a_pow_constr")
    model.addConstr(a_pow_2 * a_inv_pow_2 == 1, "a_inv_constr")

    model.addConstr(b * b == b_pow_2, "b_pow_2_constr")
    model.addConstr(b * b_pow_2 == b_pow_3, "b_pow_3_constr")
    model.addConstr(b_pow_2 * b_pow_2 == b_pow_4, "b_pow_4_constr")

    model.addConstr(c * c == c_pow_2, "c_pow_2_constr")
    model.addConstr(a_inv * c == c_over_a, "c_over_a_constr")

    testing_specific_solution = False

    if testing_specific_solution:
        vals = [-3, 3, 0]
        model.addConstr(a == vals[0])
        model.addConstr(b == vals[1])
        model.addConstr(c == vals[2])

    p_0 = c
    p_1 = a + b + c

    # know derivative is 0 at x = b/2a, so plug in that to see where min value is
    # center_val = 1 / 4 * b_pow_2 * a_inv_pow_2 - 1 / 2 * b_pow_2*a_inv + c
    # the square of the max/mininum point
    center_val_pow_2 = 1 / 16 *  b_pow_4 * a_inv_pow_2 - 1 / 2 * b_pow_2 * c_over_a + c_pow_2

    model.setObjective(p_0 * p_0 + p_1 * p_1 + center_val_pow_2, GRB.MINIMIZE)

    model.optimize()
    model.write("file.lp")
    model.write("out.sol")

    min_val = max(abs(a.x + b.x + c.x), abs(c.x), abs(b.x * b.x * ( 1 / (4 * a.x) - 1 / (2 * a.x)) + c.x))
    
    if verbose:
        print("quadratic with coefficients")
        print(a.x, b.x, c.x)
        print("obtains supremum norm: ", min_val)
        print("Optimal value is ", model.objVal)
        print("Center Val is ", b.x * b.x * ( 1 / (4 * a.x) - 1 / (2 * a.x)) + c.x)
        print("Center Val squared is ", 1 / 16 *  pow(b.x, 4) * pow(a.x, -2) - 1 / 2 * pow(b.x, 2) * c.x / a.x +  c.x * c.x)
        print("p_1 is ", pow(a.x + b.x + c.x, 2))

    GRID_SIZE = 50
    points = np.linspace(0, 1, GRID_SIZE)

    plt.plot(points, a.x * points * points + b.x * points + c.x)
    plt.xlim((-2, 2))  
    plt.ylim((-2, 2))  
    plt.axes()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()

if __name__ == "__main__":
    optimize_quadratic()
