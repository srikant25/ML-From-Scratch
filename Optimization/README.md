# 🚀 Optimization Algorithms in Machine Learning

This repository contains implementations of **various optimization techniques** used in machine learning and numerical optimization. These algorithms are foundational for training models, minimizing loss functions, and solving unconstrained optimization problems.

---

## 📌 Overview

The following optimization algorithms have been implemented from scratch:

### 🔧 List of Optimization Techniques

1. **Conjugate Gradient Algorithm**
   - Utilizes previous gradients to speed up convergence.
   - Efficient for large-scale quadratic problems.

2. **Conjugate Direction Algorithm**
   - Optimizes along conjugate directions.
   - Similar to conjugate gradient but more general.

3. **DLF Rank-1 Update**
   - A quasi-Newton method using a rank-1 approximation of the Hessian.
   - Updates the inverse Hessian approximation at each iteration.

4. **DLF Rank-2 Update**
   - Also a quasi-Newton method, but with more accurate rank-2 updates.
   - Often used to improve convergence and stability.

5. **Gradient Method (General Form)**
   - Basic form of gradient descent with customizable learning rate and direction.
   - Can serve as a base for many other methods.

6. **Gradient Method with Variable Alpha**
   - Adaptive learning rate based on iteration progress or line search.
   - Balances between speed and stability.

7. **Simple Gradient Method**
   - Classic gradient descent with fixed step size.
   - Best for convex functions and smooth surfaces.

8. **Newton’s Method**
   - Uses second-order derivatives (Hessian) for faster convergence.
   - Requires calculation or approximation of the Hessian matrix.

9. **Levenberg-Marquardt (Newton-Levenberg) Method**
   - Combines Gauss-Newton and gradient descent.
   - Particularly useful for nonlinear least squares problems.

10. **Modified Newton Method**
    - Enhances Newton’s method to handle singularities or improve stability.
    - Adds damping or regularization to avoid divergence.

---




