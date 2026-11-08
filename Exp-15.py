
import math
import matplotlib.pyplot as plt

data = [
    [4.9, 3.1, 'Setosa'],
    [5.0, 3.4, 'Setosa'],
    [5.1, 3.5, 'Setosa'],
    [6.0, 2.9, 'Versicolor'],
    [6.2, 2.8, 'Versicolor'],
    [5.9, 3.0, 'Versicolor'],
    [6.5, 3.0, 'Virginica'],
    [6.7, 3.1, 'Virginica'],
    [6.8, 3.2, 'Virginica']
]

test = [5.8, 2.9]
classes = ['Setosa', 'Versicolor', 'Virginica']
scores = {}

for cls in classes:
    rows = [r for r in data if r[2] == cls]
    prior = len(rows) / len(data)
    score = math.log(prior)

    for j in range(2):
        values = [r[j] for r in rows]
        mean = sum(values) / len(values)
        variance = sum((v - mean) ** 2 for v in values) / len(values)
        variance = max(variance, 0.01)

        probability = (1 / math.sqrt(2 * math.pi * variance)) * math.exp(
            -((test[j] - mean) ** 2) / (2 * variance)
        )
        score += math.log(probability)

    scores[cls] = score

prediction = max(scores, key=scores.get)

print("Test Flower:", test)
print("Predicted Species:", prediction)

for species in classes:
    points = [r for r in data if r[2] == species]
    plt.scatter([r[0] for r in points],
                [r[1] for r in points], label=species)

plt.scatter(test[0], test[1], color='red',
            marker='*', s=200, label='Test Flower')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Naive Bayes Classification")
plt.legend()
plt.savefig("Exp-15-Output.png")
plt.show()
