# 🔢 Numerical Linear Algebra

This repository contains Matlab implementations of key numerical linear algebra algorithms from scratch. These are foundational tools for solving linear systems, performing matrix factorization, and analyzing matrix properties in scientific computing and machine learning applications.

---

## 📘 Algorithms Implemented

### 1. **Cholesky Decomposition**
- Factorizes a symmetric, positive-definite matrix into the product of a lower triangular matrix and its transpose.
- Useful for solving systems of linear equations efficiently.

### 2. **Gauss-Seidel Algorithm**
- An iterative method for solving a system of linear equations.
- Converges faster than Jacobi in most cases.

### 3. **Jacobi Method**
- A simple iterative technique for diagonal-dominant matrices.
- Good for educational demonstration and initial approximations.

### 4. **Infinity Norm (‖·‖∞)**
- Calculates the maximum absolute row sum of a matrix.
- Useful for convergence analysis and error estimation.

### 5. **Zero Norm (‖·‖₀)**
- Counts the number of non-zero elements in a vector.
- Common in sparse matrix analysis and regularization.

### 6. **LU Factorization (without Partial Pivoting)**
- Decomposes a square matrix into a product of a lower (L) and an upper (U) triangular matrix.
- Does not involve row exchanges.

### 7. **LU Factorization (with Partial Pivoting)**
- Enhances numerical stability by including row swaps.
- Recommended for general use.

### 8. **Forward and Backward Substitution**
- Solves linear systems where the coefficient matrix is triangular.
- Used post LU or Cholesky decomposition.

### 9. **Positive Definite Matrix Check**
- Verifies whether a matrix is symmetric and all eigenvalues are positive.
- Required condition for Cholesky decomposition.

### 10. **Thomas Algorithm**
- Efficient solver for tridiagonal systems of equations.
- Linear time complexity: O(n).

### 11. **Tridiagonal Matrix Algorithm (TDMA)**
- Another name for the Thomas Algorithm.
- Common in numerical PDEs and finite difference methods.

---





