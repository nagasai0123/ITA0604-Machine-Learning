
import math
import matplotlib.pyplot as plt

data = [
    [25, 30000, 'No'],
    [30, 40000, 'No'],
    [35, 50000, 'Yes'],
    [40, 60000, 'Yes'],
    [45, 70000, 'Yes'],
    [50, 80000, 'Yes'],
    [28, 35000, 'No'],
    [38, 55000, 'Yes']
]

test = [36, 52000]
classes = ['Yes', 'No']
scores = {}

for cls in classes:
    rows = [r for r in data if r[2] == cls]
    score = math.log(len(rows) / len(data))

    for j in range(2):
        values = [r[j] for r in rows]
        mean = sum(values) / len(values)
        variance = sum((v - mean) ** 2 for v in values) / len(values)
        variance = max(variance, 1)

        probability = (1 / math.sqrt(2 * math.pi * variance)) * math.exp(
            -((test[j] - mean) ** 2) / (2 * variance)
        )
        score += math.log(probability)

    scores[cls] = score

prediction = max(scores, key=scores.get)

print("Applicant Age:", test[0])
print("Applicant Income:", test[1])
print("Loan Prediction:", prediction)

maximum = max(scores.values())
probabilities = {
    c: math.exp(scores[c] - maximum) for c in classes
}
total = sum(probabilities.values())

for c in classes:
    probabilities[c] = probabilities[c] / total * 100
    print(c, "Probability:", round(probabilities[c], 2), "%")

plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel("Loan Decision")
plt.ylabel("Probability (%)")
plt.title("Bank Loan Prediction using Naive Bayes")
plt.savefig("Exp-19-Output.png")
plt.show()
