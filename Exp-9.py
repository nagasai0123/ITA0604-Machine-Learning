
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [1, 4, 9, 16, 25]

n = len(X)

mean_x = sum(X) / n
mean_y = sum(Y) / n

m = sum((X[i] - mean_x) * (Y[i] - mean_y)
        for i in range(n)) / sum((x - mean_x) ** 2 for x in X)

c = mean_y - m * mean_x

linear = [m * x + c for x in X]
polynomial = [x ** 2 for x in X]

print("Linear Predictions:", linear)
print("Polynomial Predictions:", polynomial)

plt.scatter(X, Y, label="Actual Data")
plt.plot(X, linear, label="Linear Regression")
plt.plot(X, polynomial, label="Polynomial Regression")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.savefig("Exp-9-Output.png")
plt.show()
