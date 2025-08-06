# 📘 K-Nearest Neighbors (KNN) – Theory

## 🔍 What is KNN?

K-Nearest Neighbors (KNN) is a **non-parametric**, **instance-based** (lazy) learning algorithm used for both classification and regression.

It works by:
1. Calculating the distance between a new data point and all training points.
2. Selecting the **K closest neighbors**.
3. Predicting the output using:
   - **Majority vote** (classification)
   - **Average** (regression)

---

## 📐 Distance Metrics

KNN relies on distance to determine “closeness”. Common choices:

- **Euclidean Distance** (default):

  $$
  d(x, x') = \sqrt{\sum_{i=1}^n (x_i - x_i')^2}
  $$

- **Manhattan Distance**:
  $$
  d(x, x') = \sum_{i=1}^n |x_i - x_i'|
  $$

- **Minkowski Distance** (generalized):
  $$
  d(x, x') = \left( \sum_{i=1}^n |x_i - x_i'|^p \right)^{1/p}
  $$
  - `p = 1` → Manhattan
  - `p = 2` → Euclidean

> ⚠️ **Note**: Always scale your features before using KNN.

---

## 🧪 How KNN Classification Works?

For a new test point:
1. Compute the distance from the test point to all training points.
2. Pick the **K smallest** distances.
3. Get the labels of those K points.
4. Return the **most frequent label** among them.

---

## 🔢 Choosing the Value of K

- Small K (e.g. 1, 3): More flexible, but may overfit
- Large K (e.g. 15, 25): More stable, but may underfit

Use **cross-validation** to find the optimal `K`.

---

## ✅ Pros and ❌ Cons

### ✔️ Advantages:
- Simple and intuitive
- No training required
- Naturally handles multi-class problems
- Works well for low-dimensional data

### ❌ Disadvantages:
- Slow at prediction time (computes distances at test time)
- Sensitive to feature scaling
- Suffers from the curse of dimensionality

---

## 🌎 Real-World Analogy

Imagine you're new in town and want to find a good restaurant.  
You ask the **K nearest people** what their favorite restaurant is.  
Whichever restaurant gets the most votes — you go there. That’s KNN!

---

## 📚 Use Cases
- Recommender systems
- Handwriting recognition
- Customer segmentation
- Medical diagnosis
