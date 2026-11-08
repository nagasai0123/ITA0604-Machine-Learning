
import random
import math
import matplotlib.pyplot as plt

random.seed(10)

data = [1, 2, 2, 3, 8, 9, 10, 11]

mean1 = 2.0
mean2 = 9.0
std1 = 1.5
std2 = 1.5
weight1 = 0.5
weight2 = 0.5

def gaussian(x, mean, std):
    return (1 / (std * math.sqrt(2 * math.pi))) * math.exp(
        -((x - mean) ** 2) / (2 * std ** 2)
    )

for iteration in range(30):
    r1 = []
    r2 = []

    for x in data:
        p1 = weight1 * gaussian(x, mean1, std1)
        p2 = weight2 * gaussian(x, mean2, std2)
        total = p1 + p2

        r1.append(p1 / total)
        r2.append(p2 / total)

    sum1 = sum(r1)
    sum2 = sum(r2)

    mean1 = sum(r1[i] * data[i] for i in range(len(data))) / sum1
    mean2 = sum(r2[i] * data[i] for i in range(len(data))) / sum2

    std1 = math.sqrt(sum(
        r1[i] * (data[i] - mean1) ** 2
        for i in range(len(data))
    ) / sum1)

    std2 = math.sqrt(sum(
        r2[i] * (data[i] - mean2) ** 2
        for i in range(len(data))
    ) / sum2)

    weight1 = sum1 / len(data)
    weight2 = sum2 / len(data)

print("Mean 1:", mean1)
print("Mean 2:", mean2)
print("Weight 1:", weight1)
print("Weight 2:", weight2)

x_values = [i / 10 for i in range(0, 131)]
curve1 = [weight1 * gaussian(x, mean1, std1) for x in x_values]
curve2 = [weight2 * gaussian(x, mean2, std2) for x in x_values]

plt.hist(data, bins=8, density=True, alpha=0.5, label="Data")
plt.plot(x_values, curve1, label="Gaussian 1")
plt.plot(x_values, curve2, label="Gaussian 2")
plt.xlabel("Data")
plt.ylabel("Probability Density")
plt.title("Expectation-Maximization Algorithm")
plt.legend()
plt.savefig("Exp-10-Output.png")
plt.show()
