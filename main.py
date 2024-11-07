from src.utils import solver
import sympy as sp
if __name__ == "__main__":
    # initialize the parameter
    """
    D is the number of dimensions
    d is the highest order in polynomial
    L is the number of measures
    rho is the value of penalty term gamma
    target_value is the real minimum of the polynomial on [-1,1]^{D}
    target_relative_error is the stopping criterion for the updating of lagrangian coefficient, the iteration will stop when relative error subject to the real minimum value is less then this value
    gtol is the Stopping criterion (relative gradient) inside LBFGS, The iteration will stop when max{|proj g_i | i = 1, ..., n} <= gtol where proj g_i is the i-th component of the projected gradient.
    ftol is the Stopping criterion (absolute value) inside LBFGS,The iteration stops when (f^k - f^{k+1})/max{|f^k|,|f^{k+1}|,1} <= ftol.
    maxcor is the parameter inside LBFGS. It is the maximum number of variable metric corrections used to define the limited memory matrix. (The limited memory BFGS method does not store the full hessian but uses this many terms in an approximation to it.)
    This function will output a global mimimum point of polynomial on [-1,1]^{D} and it's relative error subject to the real minimum value
    """
    D = 3
    d = 4
    L = 6
    gamma = 100
    target_value = -1.3911
    target_relative_error = 1e-4
    gtol = 1e-6
    ftol = 1e-6
    maxcor = 40

    #input the polynomial here
    x = sp.symbols(f'x1:{D+1}')
    polynomial = (1 / D) * sum(8 * x_i**4 - 8 * x_i**2 + 1 for x_i in x) + (sum(x) / D) ** 3
    # # 构造矩阵 xx^T
    # xxT = sp.Matrix(x) * sp.Matrix(x).T
    # # # # 构造全 1 的矩阵 J，乘以 1/2
    # J = sp.Matrix([[1/2] * D] * D)
    # # # # 计算目标函数，即 Frobenius 范数的平方
    # objective_matrix = (xxT - J).applyfunc(lambda x: x**2)
    # # polynomial = sum(xi**2 for xi in x)
    # polynomial = sum(objective_matrix)
    # penalty_term = sum((xi - 1/sp.sqrt(2))**2 for xi in x)
    # polynomial +=penalty_term
    # print(polynomial)
    x_final,relative_error = solver(D,d,L,gamma,target_value,target_relative_error,gtol,ftol,maxcor,x,polynomial)
    print(x_final,relative_error)