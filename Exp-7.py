
import math
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5, 6]
Y = [0, 0, 0, 1, 1, 1]

w = 1.0
b = -3.5
lr = 0.1

for epoch in range(1000):
    dw = 0
    db = 0

    for x, y in zip(X, Y):
        z = w * x + b
        p = 1 / (1 + math.exp(-z))
        dw += (p - y) * x
        db += p - y

    w -= lr * dw / len(X)
    b -= lr * db / len(X)

print("Weight:", w)
print("Bias:", b)

def sigmoid(z):
    return 1 / (1 + math.exp(-z))

values = [i / 10 for i in range(0, 71)]
probabilities = [sigmoid(w * x + b) for x in values]

plt.scatter(X, Y, label="Training Data")
plt.plot(values, probabilities, label="Logistic Curve")
plt.xlabel("Input")
plt.ylabel("Probability")
plt.title("Logistic Regression")
plt.legend()
plt.savefig("Exp-7-Output.png")
plt.show()
