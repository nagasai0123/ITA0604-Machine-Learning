
import math
import matplotlib.pyplot as plt

data = [
    ['Sunny', 'Hot', 'No'],
    ['Sunny', 'Cool', 'Yes'],
    ['Rainy', 'Hot', 'Yes'],
    ['Rainy', 'Cool', 'Yes'],
    ['Overcast', 'Hot', 'Yes'],
    ['Overcast', 'Cool', 'Yes']
]

def entropy(rows):
    total = len(rows)
    counts = [sum(1 for r in rows if r[-1] == c)
              for c in ['Yes', 'No']]
    result = 0
    for count in counts:
        if count:
            p = count / total
            result -= p * math.log2(p)
    return result

def id3(rows, features):
    if all(r[-1] == rows[0][-1] for r in rows):
        return rows[0][-1]

    if not features:
        return max(['Yes', 'No'],
                   key=lambda c: sum(r[-1] == c for r in rows))

    gains = []
    for feature in features:
        index = feature
        values = set(r[index] for r in rows)
        remainder = sum(
            len([r for r in rows if r[index] == v]) / len(rows)
            * entropy([r for r in rows if r[index] == v])
            for v in values
        )
        gains.append((entropy(rows) - remainder, index))

    best = max(gains)[1]
    tree = {}

    for value in set(r[best] for r in rows):
        subset = [r for r in rows if r[best] == value]
        tree[value] = id3(subset, [f for f in features if f != best])

    return {best: tree}

tree = id3(data, [0, 1])
print("Decision Tree:", tree)

fig, ax = plt.subplots(figsize=(8, 5))
ax.axis('off')

ax.text(0.5, 0.9, "Outlook", ha='center',
        bbox=dict(boxstyle='round', fc='lightblue'))

positions = [(0.2, 0.55), (0.5, 0.55), (0.8, 0.55)]
labels = ['Sunny', 'Rainy', 'Overcast']

for pos, label in zip(positions, labels):
    ax.text(*pos, label, ha='center',
            bbox=dict(boxstyle='round', fc='lightgreen'))
    ax.plot([0.5, pos[0]], [0.87, pos[1] + 0.05], 'k-')

ax.text(0.2, 0.25, 'Decision: Yes / No', ha='center')
ax.text(0.5, 0.25, 'Decision: Yes', ha='center')
ax.text(0.8, 0.25, 'Decision: Yes', ha='center')

plt.title("ID3 Decision Tree")
plt.savefig("Exp-3-Output.png")
plt.show()
