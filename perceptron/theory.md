# Perceptron
It is a linear model, meaning it finds a straight line(or a hyperplane in higher dimensions) that separates the two classes.

 ### Prediction Rule:

$$
\hat{y} = 
\begin{cases}
1 & \text{if } w^Tx + b \geq 0 \\
-1 & \text{otherwise } 
\end{cases}
$$

Alternate,
$$
\hat{y} = 
\begin{cases}
1 & \text{if } w^Tx + b \geq 0 \\
0 & \text{otherwise } 
\end{cases}
$$


where, 

- $w$ : weights vector
- $x$ : input vector
- $b$ : bias

### Update Rule (for every misclassification):

$$
w = w + \eta . y.x \\
b = b + \eta . y
$$

Alternate,

$$
w = w + \eta . (y - \hat{y}).x \\
b = b + \eta . (y - \hat{y})
$$

where,

- $\eta$ : learning rate
- $y$ : true label
- $\hat{y}$ : predicted label

>**Q: What is misclasification or when does it happen?** 
>
> It happens when actual label is different from predicted label.
> - **$y = \hat{y}$** :  no update required
>$$
>\text{case 1 : } (1-1) = 0 \\
>\text{case 2 : } (0-0) = 0
>
>$$ 
> - **$y \neq \hat{y}$** : update weights
>$$
>\text{case 1 : } (1-0) = 1 \text{, increase the weights}\\
>\text{case 2 : } (0-1) = -1 \text{, decrease the weights}
>
>
>$$

