
import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]
Y = [2, 4, 5, 4, 6]

n = len(X)
mean_x = sum(X) / n
mean_y = sum(Y) / n

numerator = sum((X[i] - mean_x) * (Y[i] - mean_y)
                for i in range(n))
denominator = sum((x - mean_x) ** 2 for x in X)

m = numerator / denominator
c = mean_y - m * mean_x

predictions = [m * x + c for x in X]

print("Slope:", m)
print("Intercept:", c)
print("Predictions:", predictions)

plt.scatter(X, Y, label="Actual Data")
plt.plot(X, predictions, label="Regression Line")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.legend()
plt.savefig("Exp-8-Output.png")
plt.show()
