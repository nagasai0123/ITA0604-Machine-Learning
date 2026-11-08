
import matplotlib.pyplot as plt

data = [
    [20, 10, 'Good'],
    [25, 15, 'Good'],
    [30, 20, 'Good'],
    [50, 60, 'Poor'],
    [60, 70, 'Poor'],
    [70, 80, 'Poor']
]

test = [35, 25]
k = 3

distances = []
for row in data:
    d = ((row[0] - test[0]) ** 2 +
         (row[1] - test[1]) ** 2) ** 0.5
    distances.append((d, row[2]))

distances.sort()
neighbors = distances[:k]

prediction = max(set(n[1] for n in neighbors),
                 key=lambda c: sum(n[1] == c for n in neighbors))

print("Test Data:", test)
print("Predicted Credit Score:", prediction)

for label, marker in [('Good', 'o'), ('Poor', 's')]:
    points = [r for r in data if r[2] == label]
    plt.scatter([r[0] for r in points],
                [r[1] for r in points],
                marker=marker, label=label)

plt.scatter(test[0], test[1], color='red',
            marker='*', s=200, label='New Customer')
plt.xlabel("Income")
plt.ylabel("Debt Ratio")
plt.title("Credit Score Classification using KNN")
plt.legend()
plt.savefig("Exp-11-Output.png")
plt.show()
