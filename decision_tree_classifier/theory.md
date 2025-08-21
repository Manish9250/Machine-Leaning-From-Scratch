# Decision Tree Classifier – Theory

## 1. What is a Decision Tree?
A **Decision Tree** is a supervised learning algorithm used for **classification** and **regression** tasks.  
It works like a flowchart:  
- Each **internal node** represents a decision on a feature.  
- Each **branch** represents the outcome of that decision.  
- Each **leaf node** represents a final prediction (class label in classification).  

Example (for classification):  
```
Is Age < 30?
├── Yes → Class A
└── No
    └── Income > 50K?
        ├── Yes → Class B
        └── No → Class C
```

---

## 2. Impurity Measures
When splitting data, the goal is to make subsets as "pure" as possible (each subset should ideally contain only one class).

### (a) Gini Index (used by CART – Classification and Regression Trees)
$$
Gini = 1 - \sum_{i=1}^{C} p_i^2
$$
- $p_i$ = proportion of class $i$ in the node  
- Range: $0 \to 1$  
- **0 = pure node**, higher = more impure  

### (b) Entropy (used in ID3, C4.5)
$$
Entropy = - \sum_{i=1}^{C} p_i \log_2(p_i)
$$
- Information Gain (IG) is used to decide splits:
$$
IG = Entropy(parent) - \sum_{children} \frac{N_j}{N} \times Entropy(child_j)
$$

Both Gini and Entropy usually give similar results.  

---

## 3. Decision Tree Algorithm (Classification)
1. Start with all training samples at the **root**.  
2. For each feature:  
   - Try possible split points.  
   - Compute impurity (Gini/Entropy) of resulting subsets.  
   - Choose the split that minimizes impurity.  
3. Split the dataset into subsets.  
4. Repeat recursively for each subset until:  
   - Maximum depth is reached, OR  
   - All samples in a node belong to one class, OR  
   - No further meaningful split is possible.  

---

## 4. Prediction
To predict the class of a sample:
- Start at the **root**.  
- Traverse the tree by checking feature values.  
- End at a **leaf node**.  
- Predict the **majority class** of that leaf.  

---

## 5. Advantages & Disadvantages
✅ Easy to understand & interpret  
✅ Handles both numerical & categorical data  
✅ Non-linear decision boundaries  

❌ Prone to overfitting (deep trees)  
❌ Small changes in data → different trees  
❌ Biased towards features with many split points  

---
