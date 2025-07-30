# Linear Regression
- ### Goal
Linear regression is used to predict continuous outcomes based on one or more input features.

- ### Simple Linear Regression Equation

$$
\hat{y} = wX + b
$$

where: 
- X : input features
- w : weight(slope)
- b : bias(intercept)
- $\hat{y}$ : predicted ouput

- ### Objective
minimize the **Mean Squared Error (MSE)** between predicted and actual values:

$$
MSE = \frac{1}{n} \sum_{i=1}^{n} (\hat{y}_i - y_i)^2
$$

- ### Solution
we can solve this directly using normal equation:

$$
\theta = (X^TX)^{-1}X^Ty
$$

where: 
- X is the input matrix(with a column of 1s for bias)
- y is the output vector
- $\theta = [w \; b]^T$