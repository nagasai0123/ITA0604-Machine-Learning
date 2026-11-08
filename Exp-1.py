
import matplotlib.pyplot as plt

# FIND-S Algorithm

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

hypothesis = ['0'] * 6

for row in data:
    if row[-1] == 'Yes':
        for i in range(6):
            if hypothesis[i] == '0':
                hypothesis[i] = row[i]
            elif hypothesis[i] != row[i]:
                hypothesis[i] = '?'

print("FIND-S Algorithm")
print("Final Hypothesis:", hypothesis)

# Display graphical output
features = ['Sky', 'AirTemp', 'Humidity',
            'Wind', 'Water', 'Forecast']

plt.figure(figsize=(9, 4))
plt.axis('off')

table = plt.table(
    cellText=[hypothesis],
    colLabels=features,
    loc='center',
    cellLoc='center'
)

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1, 2)

plt.title("FIND-S Final Hypothesis")
plt.savefig("Exp-1-Output.png", dpi=200, bbox_inches="tight")
plt.show()
