
import matplotlib.pyplot as plt

data = [
    [4.9, 3.0, 0],
    [5.0, 3.2, 0],
    [5.1, 3.5, 0],
    [5.4, 3.4, 0],
    [6.0, 2.8, 1],
    [6.2, 2.9, 1],
    [6.4, 3.2, 1],
    [6.5, 3.0, 1]
]

w1 = 0
w2 = 0
bias = 0
learning_rate = 0.1

for epoch in range(50):
    for x1, x2, target in data:
        output = 1 if w1*x1 + w2*x2 + bias >= 0 else 0
        error = target - output

        w1 += learning_rate * error * x1
        w2 += learning_rate * error * x2
        bias += learning_rate * error

print("Weight 1:", w1)
print("Weight 2:", w2)
print("Bias:", bias)

for label, marker in [(0, 'o'), (1, 's')]:
    points = [r for r in data if r[2] == label]
    plt.scatter([r[0] for r in points],
                [r[1] for r in points],
                marker=marker, label='Class ' + str(label))

x_values = [4.5 + i * 0.05 for i in range(50)]

if w2 != 0:
    y_values = [-(w1*x + bias) / w2 for x in x_values]
    plt.plot(x_values, y_values, label="Decision Boundary")

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Perceptron Iris Classification")
plt.legend()
plt.savefig("Exp-18-Output.png")
plt.show()
