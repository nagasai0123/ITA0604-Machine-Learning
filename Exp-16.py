
import matplotlib.pyplot as plt

actual = [0, 0, 1, 1, 0, 1, 0, 1]

knn = [0, 0, 1, 1, 0, 1, 1, 1]
naive_bayes = [0, 1, 1, 1, 0, 1, 0, 1]
decision_tree = [0, 0, 1, 0, 0, 1, 0, 1]

def accuracy(actual, predicted):
    correct = sum(a == p for a, p in zip(actual, predicted))
    return correct / len(actual) * 100

scores = [
    accuracy(actual, knn),
    accuracy(actual, naive_bayes),
    accuracy(actual, decision_tree)
]

print("KNN Accuracy:", scores[0], "%")
print("Naive Bayes Accuracy:", scores[1], "%")
print("Decision Tree Accuracy:", scores[2], "%")

algorithms = ['KNN', 'Naive Bayes', 'Decision Tree']

plt.bar(algorithms, scores)
plt.ylim(0, 110)
plt.ylabel("Accuracy (%)")
plt.title("Classification Algorithm Comparison")

for i, score in enumerate(scores):
    plt.text(i, score + 2, str(round(score, 2)) + "%", ha='center')

plt.savefig("Exp-16-Output.png")
plt.show()
