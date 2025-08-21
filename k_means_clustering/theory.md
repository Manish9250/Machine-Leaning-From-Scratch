# K-Means Clustering — Theory

K-Means is an **unsupervised** clustering algorithm that partitions `n` samples into `K` clusters by minimizing within-cluster variance (sum of squared distances to the cluster centroids).

---

## Objective Function (Inertia)

Given data points $X = \{x_1, x_2, \dots, x_n\} \subset \mathbb{R}^d$, K-Means seeks centroids $C = \{\mu_1, \dots, \mu_K\}$ and an assignment function $a(i) \in \{1, \dots, K\}$ that minimize the **inertia**:

$$
J(C, a) = \sum_{i=1}^{n} \lVert x_i - \mu_{a(i)} \rVert_2^2.
$$

Lower inertia indicates tighter clusters. Note: inertia always decreases (or stays the same) across iterations and is bounded below by 0, so the algorithm converges.

---

## Algorithm (Lloyd’s Algorithm)

1. **Initialize centroids** $\mu_1, \dots, \mu_K$ (randomly or with k-means++).
2. **Assignment step** (E-step-like): assign each point to its nearest centroid by Euclidean distance.
3. **Update step** (M-step-like): recompute each centroid as the mean of points assigned to it.
4. **Repeat** steps 2–3 until convergence (centroids move less than a tolerance) or a maximum number of iterations is reached.

This alternates between minimizing w\.r.t. assignments and centroids, guaranteeing monotonic decrease of $J$, but only to a **local** minimum.

---

## Initialization Strategies

* **Random**: pick $K$ distinct points uniformly at random as initial centroids.
* **k-means++**: probabilistic seeding that spreads initial centroids apart to reduce poor local minima and speed up convergence.

**k-means++** procedure:

1. Choose the first centroid uniformly at random from the data.
2. For each point $x$, compute $D(x)^2$: squared distance to the nearest chosen centroid.
3. Choose the next centroid with probability proportional to $D(x)^2$.
4. Repeat until $K$ centroids are chosen.

---

## Distance Metric

Standard K-Means uses **Euclidean distance**. With Euclidean distance, the cluster mean minimizes within-cluster squared error. Other distances (e.g., Manhattan) lead to different update rules (e.g., medians), and are outside classic K-Means.

---

## Convergence Criteria

* **Centroid shift**: stop if total movement of centroids is below `tol`.
* **No change in assignments**: labels don’t change between iterations.
* **Max iterations**: safety cap to stop.

K-Means complexity per iteration is roughly $\mathcal{O}(n K d)$. Let `it` be the number of iterations; total is $\mathcal{O}(n K d \cdot it)$.

---

## Choosing K

Common heuristics (no single right answer):

* **Elbow method**: plot inertia vs. `K` and look for a “knee”.
* **Silhouette score**: measures how similar a point is to its own cluster vs. others; ranges from −1 to 1.
* **Domain knowledge**: expected number of natural groups.

---

## Data Preprocessing

* **Feature scaling**: Standardize or normalize features so that dimensions with large scales don’t dominate Euclidean distance.
* **Outliers**: large effect on means and distances; consider robust scaling or outlier handling.

---

## Edge Cases & Practical Details

* **Empty clusters**: occasionally a centroid gets no points. Options:

  * Reinitialize that centroid (e.g., to the farthest point from all current centroids),
  * Drop the cluster (reduces `K`), or
  * Split the largest cluster.
* **Duplicate points**: fine; random tie-breaking in assignment.
* **Non-spherical clusters**: K-Means struggles with elongated or varying-density clusters.
* **Multiple initializations (`n_init`)**: run K-Means several times with different seeds; keep the solution with the lowest inertia.
* **Mini-batch K-Means**: stochastic approximation using small random batches for scalability.

---

## When to Use K-Means

* You expect roughly spherical, similarly sized clusters.
* You need a fast, simple baseline for partitioning data.
* You can reasonably standardize features and pick `K` (or explore a small range of `K`).

---

## Outputs

* **`cluster_centers_`**: the learned centroids (shape: `K × d`).
* **`labels_`**: cluster index (0..K−1) for each sample.
* **`inertia_`**: final within-cluster sum of squares.

---

## Pseudocode

```
choose initial centroids μ₁..μ_K
repeat until convergence or max_iter:
    # Assign
    for each xᵢ:
        a(i) ← argmin_k ||xᵢ − μ_k||²
    # Update
    for each k:
        μ_k ← mean({xᵢ | a(i) = k})
return μ, a, inertia
```

---

## Tips

* Set `random_state` for reproducibility.
* Start with `k-means++`, `n_init > 1`, and standardized features.
* Inspect inertia vs. `K` and optionally silhouette scores.
