
import math
import matplotlib.pyplot as plt

X = [[1, 2], [2, 3], [3, 3], [6, 7],
     [7, 8], [8, 7]]
Y = ['A', 'A', 'A', 'B', 'B', 'B']

test = [5, 6]
k = 3

distances = []

for point, label in zip(X, Y):
    d = math.sqrt((point[0] - test[0]) ** 2 +
                  (point[1] - test[1]) ** 2)
    distances.append((d, label, point))

distances.sort()
neighbors = distances[:k]

prediction = max(set(n[1] for n in neighbors),
                 key=lambda c: sum(n[1] == c for n in neighbors))

print("Test Point:", test)
print("Nearest Neighbours:", [(n[2], n[1]) for n in neighbors])
print("Predicted Class:", prediction)

for label, marker in [('A', 'o'), ('B', 's')]:
    points = [p for p, y in zip(X, Y) if y == label]
    plt.scatter([p[0] for p in points],
                [p[1] for p in points],
                marker=marker, label=label)

plt.scatter(test[0], test[1], color='red',
            marker='*', s=200, label='Test Point')

for n in neighbors:
    p = n[2]
    plt.plot([test[0], p[0]], [test[1], p[1]], 'k--')

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Nearest Neighbours")
plt.legend()
plt.savefig("Exp-5-Output.png")
plt.show()
