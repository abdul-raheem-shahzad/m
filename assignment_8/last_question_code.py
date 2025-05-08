import numpy as np

def simplex(c, A, b):
    """
    Solve: maximize c^T x  subject to A x <= b, x >= 0.
    Returns (x_opt, max_value).
    """
    m, n = A.shape
    # Build tableau [ A | I | b ]
    tableau = np.zeros((m+1, n + m + 1))
    tableau[:m, :n]        = A
    tableau[:m, n:n+m]     = np.eye(m)
    tableau[:m, -1]        = b
    tableau[-1, :n]        = -c   # objective row

    basis = list(range(n, n+m))

    while True:
        # Check for optimality
        if np.all(tableau[-1, :-1] >= 0):
            break
        # Entering variable (most negative coeff)
        j = np.argmin(tableau[-1, :-1])
        col = tableau[:-1, j]
        if np.all(col <= 0):
            raise Exception("Unbounded LP")
        # Minimum ratio test
        ratios = tableau[:-1, -1] / col
        ratios[col <= 0] = np.inf
        i = np.argmin(ratios)
        # Pivot operation
        pivot = tableau[i, j]
        tableau[i, :] /= pivot
        for k in range(m+1):
            if k != i:
                tableau[k, :] -= tableau[k, j] * tableau[i, :]
        basis[i] = j

    # Extract solution
    x = np.zeros(n + m)
    x[basis] = tableau[:-1, -1]
    return x[:n], tableau[-1, -1]

# Problem data
c = np.array([200, 300])
A = np.array([[1,1], [3,2], [2,4]])
b = np.array([45, 100, 120])

# Solve
(sol, max_profit) = simplex(c, A, b)
print(f"Wheat acres: {sol[0]:.0f}")
print(f"Corn  acres: {sol[1]:.0f}")
print(f"Max profit:  ${max_profit:.2f}")
