# 📊 Naive Bayes Classifier

Naive Bayes is a **probabilistic classification algorithm** based on **Bayes' Theorem**, assuming that features are **independent** given the class (this is the "naive" part).

---

## 🔢 Bayes' Theorem

$$
P(Y|X) = \frac{P(X|Y) \cdot P(Y)}{P(X)}
$$

Where:
- $ P(Y|X)$: Posterior probability of class given features
- $ P(X|Y)$: Likelihood of features given class
- $ P(Y)$: Prior probability of class
- $ P(X)$: Evidence (can be ignored in classification)

---

## 💡 Key Idea

For a given input $ X = (x_1, x_2, ..., x_n) $, we calculate:

$$
\hat{y} = \arg\max_y \left[ P(y) \prod_{i=1}^{n} P(x_i | y) \right]
$$

- We assume all features $ x_i $ are **conditionally independent**.
- The classifier selects the class $ y $ that **maximizes** the posterior probability.

---

## 📚 Types of Naive Bayes

- **Gaussian Naive Bayes**: For continuous features (assumes normal distribution).
- **Multinomial Naive Bayes**: For discrete counts (e.g., text classification).
- **Bernoulli Naive Bayes**: For binary features.

---

## ✅ Applications
- Spam filtering
- Sentiment analysis
- Text classification

# 📘 Gaussian Naive Bayes - Theory
It is called *Gaussian* because it assumes that the continuous features follow a **normal (Gaussian) distribution**.

---

## 🎯 Classification Goal

We aim to find the class `y` that maximizes the posterior:

$$
\hat{y} = \arg\max_y \, P(y) \cdot \prod_{i=1}^{n} P(x_i | y)
$$

Each feature $ x_i $ is assumed to be **independent**, hence the product of likelihoods.

---

### 📈 1. Gaussian Likelihood

For continuous features, we assume:

$$
P(x_i | y) = \frac{1}{\sqrt{2\pi\sigma_y^2}} \cdot \exp\left( -\frac{(x_i - \mu_y)^2}{2\sigma_y^2} \right)
$$

Where:
- $\mu_y $: Mean of feature $ x_i $ for class `y`
- $ \sigma_y^2 $: Variance of feature $ x_i $ for class `y`

This formula is applied to **each feature and class** during training.


---

### ✅ Advantages

- Very fast to train and predict
- Works well with high-dimensional data
- Handles binary and multiclass problems
- Great for text classification tasks

---

### ⚠️ Limitations

- The independence assumption rarely holds in real data
- Performance may degrade with highly correlated features
- The Gaussian assumption might not fit all feature distributions

---

### 📦 2. Multinomial Naive Bayes

- **Used for:** Text classification (e.g., spam detection), document classification
- **Assumes:** Features represent **discrete frequency counts** (e.g., word counts)
- **Likelihood:** Probability of feature occurring a certain number of times, given a class.

#### 📌 Formula:

$$
P(X | y) = \prod_{i=1}^{n} P(x_i | y)^{x_i}
$$

- Where $ x_i $ is the **count** of feature $ i $, and $ P(x_i | y) $ is estimated as:

$$
P(x_i | y) = \frac{\text{count of feature } x_i \text{ in class } y + \alpha}{\text{total count of all features in class } y + \alpha \cdot n}
$$

- $ \alpha $ is the **smoothing parameter** (Laplace smoothing).

---

### ✅ When to Use Multinomial NB?

- You have **word counts**, term frequencies, or document vectors (e.g., from `CountVectorizer`)
- Features are **non-negative integers**

---

### 🟩 3. Bernoulli Naive Bayes

- **Used for:** Binary/Boolean features (presence or absence)
- **Assumes:** Each feature is a **binary indicator** (0 or 1)

#### 📌 Formula:

$$
P(X | y) = \prod_{i=1}^{n} P(x_i = 1 | y)^{x_i} \cdot (1 - P(x_i = 1 | y))^{1 - x_i}
$$

- Suitable when we care whether a word appeared or not (not how many times).

---

### ✅ When to Use Bernoulli NB?

- You’re working with binary features (e.g., word present or not)
- Common with `TfidfVectorizer(binary=True)` or binary bag-of-words models

---

### 🧠 Key Differences

| Feature Type   | Model               | Use Case                  |
|----------------|---------------------|---------------------------|
| Continuous     | Gaussian NB         | Numeric features          |
| Counts         | Multinomial NB      | Text classification       |
| Binary         | Bernoulli NB        | Spam filtering, yes/no    |

---


