# 📘 Soft-Margin SVM — Theory & Derivation

We want to find a hyperplane:

$$f(x) = w^T x + b$$

that separates data with the **largest margin**.

---

## 1. Hard Margin (perfectly separable case)

Optimization problem:

$$min_{w,b} (1/2) * ||w||^2$$


subject to:

$$y_i (w^T x_i + b) >= 1, for all i
$$

- Ensures margin = `1 / ||w||`.
- Fails when classes overlap.

---

## 2. Soft Margin (realistic case)

Introduce **slack variables** `ξ_i >= 0` to allow violations:
$$
y_i (w^T x_i + b) >= 1 - ξ_i
$$
- $ξᵢ = 0 →$ correctly classified and outside margin  
- $0 < ξᵢ < 1 →$ inside margin, but still correct side  
- $ξᵢ > 1 →$ misclassified point  

---

## 3. New Optimization Problem

We now minimize both:
- Large weights (small ||w||²) → wide margin  
- Total slack (Σ ξᵢ) → fewer violations  
$$
min_{w, b, ξ} (1/2) * ||w||^2 + C * Σ ξ_i
$$
subject to:
$$
y_i (w^T x_i + b) >= 1 - ξ_i
ξ_i >= 0
$$

- `C > 0`: regularization parameter (penalty for misclassification).  
  - Large C → less tolerance, stricter  
  - Small C → more tolerance, wider margin  

---

## 4. Hinge Loss Form

Instead of explicitly using ξᵢ, we reformulate with **hinge loss**:
$$
Loss(w, b) = (1/2) * ||w||^2 + C * Σ max(0, 1 - y_i (w^T x_i + b))
$$
- If correctly classified with margin ≥ 1 → loss = 0  
- Otherwise → loss increases linearly with violation  

---

## 5. Gradient (for Implementation)

We minimize:
$$
J(w, b) = (1/2) * ||w||^2 + C * Σ max(0, 1 - y_i (w^T x_i + b))
$$


Case 1: if `y_i (w^T x_i + b) >= 1`
$$∇w = w$$
$$
∇b = 0
$$
Case 2: if `y_i (w^T x_i + b) < 1`
$$∇w = w - C * y_i * x_i$$
$$∇b = -C * y_i
$$
So we can use **gradient descent / SGD** to learn `w, b`.

---
