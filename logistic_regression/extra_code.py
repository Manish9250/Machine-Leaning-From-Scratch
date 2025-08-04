# Log-loss funtion
import matplotlib.pyplot as plt
import numpy as np


p = np.linspace(0.001, 0.999, 200)  # Avoid log(0)
loss_y1 = -np.log(p)                # when y = 1
loss_y0 = -np.log(1 - p)            # when y = 0

plt.figure(figsize=(6, 4))
plt.plot(p, loss_y1, label='y=1')
plt.plot(p, loss_y0, label='y=0')
plt.title('Log Loss Function')
plt.xlabel('Predicted Probability')
plt.ylabel('Loss')
plt.grid(True)
plt.legend()
plt.savefig('log_loss_plot.png')  # Save as image
plt.show()


# Sigmoid function
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# Plot
z = np.linspace(-10, 10, 200)
s = sigmoid(z)

plt.figure(figsize=(6, 4))
plt.plot(z, s, label='Sigmoid')
plt.title('Sigmoid Function')
plt.xlabel('z')
plt.ylabel('σ(z)')
plt.grid(True)
plt.axvline(0, color='gray', linestyle='--', alpha=0.5)
plt.axhline(0.5, color='gray', linestyle='--', alpha=0.5)
plt.legend()
plt.savefig('sigmoid_plot.png')  # Save as image
plt.show()
