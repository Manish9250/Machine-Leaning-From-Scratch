# Principal Component Analysis (PCA)

## Introduction
Principal Component Analysis (PCA) is a **dimensionality reduction** technique used to reduce the number of features in a dataset while retaining as much variance (information) as possible.  
It works by projecting data into a new set of orthogonal axes (principal components), ordered by the amount of variance they capture.

---

## Key Ideas
1. **Variance** → PCA tries to capture directions of maximum variance in data.  
2. **Orthogonality** → Each principal component is orthogonal (perpendicular) to the previous ones.  
3. **Ranking** → First principal component (PC1) captures the most variance, the second (PC2) captures the next most, and so on.  

---

## Steps in PCA
1. **Standardize / Center the Data**
   - Subtract the mean of each feature so that data is centered at zero.
   - (Optional: scale by standard deviation if features are on different scales).

2. **Compute Covariance Matrix**
   - The covariance matrix measures how features vary together.
   - For two features X and Y:
     $$
     Cov(X, Y) = \frac{1}{n-1} \sum (X_i - \bar{X})(Y_i - \bar{Y})
     $$

3. **Compute Eigenvalues & Eigenvectors**
   - Solve:
     $$
     \Sigma v = \lambda v
     $$
     where:
     - $ \Sigma $ = covariance matrix
     - $ v $ = eigenvector (direction of principal component)
     - $ \lambda $ = eigenvalue (amount of variance captured by that component)

4. **Sort Eigenvectors**
   - Sort eigenvectors by decreasing eigenvalues.
   - Eigenvalues tell us **how much variance** each principal component explains.

5. **Project Data**
   - Transform original data into the new subspace:
     $$
     Z = X \cdot W
     $$
     where $ W $ = matrix of selected eigenvectors.

---

## Interpretation
- **Eigenvectors** → directions (axes) of new features (principal components).  
- **Eigenvalues** → amount of variance explained by each eigenvector.  
- **Explained Variance Ratio** → how much information each component retains.

---

## Example
- Suppose we have 2D data (X1, X2).  
- PCA finds a new axis PC1 (maximum variance direction).  
- PC2 is perpendicular to PC1 and captures remaining variance.  
- If most variance is in PC1, we can reduce 2D → 1D while still keeping most information.

---

## When to Use PCA
- When data has **high dimensionality**.  
- To reduce noise and redundancy.  
- For visualization in 2D/3D.  
- As a preprocessing step before ML models.

---

## Limitations
- PCA is **linear** → it cannot capture nonlinear structures.  
- Harder to interpret transformed features.  
- Sensitive to feature scaling (standardization is often required).

