
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
k = 3

distances = []
for row in data:
    d = math.sqrt((row[0] - test[0]) ** 2 +
                  (row[1] - test[1]) ** 2)
    distances.append((d, row[2]))

distances.sort()
neighbors = distances[:k]

prediction = max(set(n[1] for n in neighbors),
                 key=lambda c: sum(n[1] == c for n in neighbors))

print("Test Flower:", test)
print("Predicted Species:", prediction)

for species in ['Setosa', 'Versicolor', 'Virginica']:
    points = [r for r in data if r[2] == species]
    plt.scatter([r[0] for r in points],
                [r[1] for r in points], label=species)

plt.scatter(test[0], test[1], color='red',
            marker='*', s=200, label='Test Flower')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Iris Classification using KNN")
plt.legend()
plt.savefig("Exp-12-Output.png")
plt.show()
