
import random
import matplotlib.pyplot as plt

random.seed(1)

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
Y = [0, 1, 1, 0]

def sigmoid(x):
    return 1 / (1 + 2.71828 ** (-x))

w1 = [[random.uniform(-1, 1) for _ in range(2)] for _ in range(2)]
w2 = [random.uniform(-1, 1) for _ in range(2)]
b1 = [0.0, 0.0]
b2 = 0.0
lr = 0.5
losses = []

for epoch in range(5000):
    total_loss = 0

    for x, target in zip(X, Y):
        h = [sigmoid(sum(x[i] * w1[j][i] for i in range(2)) + b1[j])
             for j in range(2)]

        output = sigmoid(sum(h[j] * w2[j] for j in range(2)) + b2)
        error = output - target
        total_loss += error ** 2

        delta2 = error * output * (1 - output)
        delta1 = [delta2 * w2[j] * h[j] * (1 - h[j])
                  for j in range(2)]

        for j in range(2):
            w2[j] -= lr * delta2 * h[j]
            b1[j] -= lr * delta1[j]
            for i in range(2):
                w1[j][i] -= lr * delta1[j] * x[i]

        b2 -= lr * delta2

    losses.append(total_loss / 4)

print("XOR Predictions:")
for x in X:
    h = [sigmoid(sum(x[i] * w1[j][i] for i in range(2)) + b1[j])
         for j in range(2)]
    output = sigmoid(sum(h[j] * w2[j] for j in range(2)) + b2)
    print(x, ":", round(output))

plt.plot(losses)
plt.xlabel("Epochs")
plt.ylabel("Mean Squared Error")
plt.title("ANN Backpropagation Training")
plt.savefig("Exp-4-Output.png")
plt.show()
