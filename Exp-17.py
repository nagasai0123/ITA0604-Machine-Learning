
import math
import matplotlib.pyplot as plt

data = [
    [2, 3000, 'Low'],
    [3, 3500, 'Low'],
    [4, 4000, 'Medium'],
    [6, 4500, 'Medium'],
    [8, 5000, 'High'],
    [12, 6000, 'High']
]

test = [6, 4200]
k = 3

distances = []

for row in data:
    d = math.sqrt((row[0] - test[0]) ** 2 +
                  ((row[1] - test[1]) / 1000) ** 2)
    distances.append((d, row[2]))

distances.sort()
neighbors = distances[:k]

prediction = max(set(n[1] for n in neighbors),
                 key=lambda c: sum(n[1] == c for n in neighbors))

print("RAM:", test[0], "GB")
print("Battery:", test[1], "mAh")
print("Predicted Price Range:", prediction)

for label in ['Low', 'Medium', 'High']:
    points = [r for r in data if r[2] == label]
    plt.scatter([r[0] for r in points],
                [r[1] for r in points], label=label)

plt.scatter(test[0], test[1], color='red',
            marker='*', s=200, label='New Mobile')
plt.xlabel("RAM (GB)")
plt.ylabel("Battery (mAh)")
plt.title("Mobile Price Prediction using KNN")
plt.legend()
plt.savefig("Exp-17-Output.png")
plt.show()
