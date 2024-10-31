# product-measures
# Polynomial Optimization with Augmented Lagrangian Method

This repository provides a Python-based solution to finding the global minimum of a polynomial over the domain \([-1, 1]^D\) using the Augmented Lagrangian Method. The code leverages symbolic computation and matrix restoration to implement constrained optimization, making it ideal for polynomials with specific matrix constraints.

## Overview of Code Functions

### 1. Generate Symbolic Coefficients of the Polynomial
- **Function**: `g_D_symbolic_coefficients`
  - **Input**: Polynomial expression and symbolic variable `x`.
  - **Output**: Extracts the ordered terms of the polynomial and their corresponding coefficients, stored in dictionaries (`orders_list` and `coefficients_list`). This information is essential for evaluating polynomial values in subsequent calculations.
  - **Purpose**: Expands the polynomial and extracts each term's power and coefficient, storing these in a dictionary format for easier computation.

### 2. Matrix Restoration Functions
- **Function**: `restore_matrices`
  - **Input**: Flattened input `s`, polynomial degree `d`, dimensions `D`, and number of measures `L`.
  - **Output**: Restores `s` into two lists of matrices, `x_mu_D_L_list` and `x_R_L_list`, representing parameter matrices for measures and matrix product terms, respectively.
  - **Supporting Function**: `generate_M_d`
    - Converts `x_mu_D_L_list` into \( M_d \) matrices.
  - **Purpose**: Reconstructs matrix structures from the flattened input for accurate calculations within the Augmented Lagrangian Method.

### 3. Augmented Lagrangian Function Calculation
- **Function**: `Augmented_Lagrangian` and `Augmented_Lagrangian_without_objective`
  - **Input**: Variables `x_input`, `d`, `D`, `L`, list of polynomial terms (`orders_list`), coefficients (`coefficients_list`), Lagrangian coefficients, and penalty term `rho`.
  - **Output**: Computes the value of the Augmented Lagrangian function.
  - **Sub-functions**:
    - `term_1`: Calculates polynomial terms.
    - `term_2`: Computes the Lagrangian terms.
    - `term_3`: Computes penalty terms.
  - **Purpose**: Calculates the value of the augmented Lagrangian function, summing up the polynomial, Lagrangian, and penalty terms. This function defines the core optimization objective.

### 4. Updating Lagrange Coefficients
- **Function**: `update_Lagrangian_coefficients`
  - **Input**: Parameters for polynomial degree `d`, dimensions `D`, measures `L`, input `x_input`, Lagrange coefficients, and penalty term `rho`.
  - **Output**: Updates the Lagrange multipliers for constraints based on the values in `x_mu_D_L_list` and `x_R_L_list`.
  - **Purpose**: Applies the penalty term `rho` to update Lagrange multipliers, enforcing constraints like $\(\mu_{(1,0)}^l \geq 0\)$ by comparing with zero to ensure non-negativity.

### 5. Gradient Calculation
- **Function**: `jac_term1_new`
  - **Input**: Flattened input `x_input`, degree `d`, dimensions `D`, measures `L`, and lists of polynomial terms and coefficients.
  - **Output**: Returns the Jacobian of `term_1`.
  - **Purpose**: Optimizes gradient calculation for `term_1`, reducing redundant computations and storing Jacobian values to be used within the optimization process.

### 6. Solver
- **Function**: `solver`
  - **Input**: Parameters including polynomial dimensions `D`, degree `d`, measures `L`, penalty term `rho`, target minimum value (`target_value`), target relative error (`target_relative_error`), L-BFGS parameters (`gtol`, `ftol`, `maxcor`), polynomial expression, and symbolic variable `x`.
  - **Output**: Computes the global minimum point of the polynomial and the relative error compared to the actual minimum value.
  - **Purpose**: Implements the L-BFGS optimization method to minimize the Augmented Lagrangian function, iteratively updating `x_input` and adjusting `Lagrangian_coefficient` and `rho`. The solver stops when the relative error is less than `target_relative_error` or other stopping criteria are met.


# How to play
Clone this repo and open main.py
