
import matplotlib.pyplot as plt

actual = ['Yes', 'Yes', 'No', 'No', 'Yes', 'No']
predicted = ['Yes', 'Yes', 'No', 'Yes', 'Yes', 'No']

labels = ['Yes', 'No']
matrix = [[0, 0], [0, 0]]

for a, p in zip(actual, predicted):
    matrix[labels.index(a)][labels.index(p)] += 1

accuracy = sum(matrix[i][i] for i in range(2)) / len(actual) * 100

print("Confusion Matrix:", matrix)
print("Accuracy:", accuracy, "%")

plt.imshow(matrix, cmap='Blues')
plt.xticks([0, 1], labels)
plt.yticks([0, 1], labels)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Naive Bayes Confusion Matrix")

for i in range(2):
    for j in range(2):
        plt.text(j, i, matrix[i][j],
                 ha='center', va='center')

plt.colorbar()
plt.savefig("Exp-6-Output.png")
plt.show()
