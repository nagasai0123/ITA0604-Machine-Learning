
import matplotlib.pyplot as plt

data = [
    ['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', 'Yes'],
    ['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', 'No'],
    ['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', 'Yes']
]

S = ['0'] * 6
G = ['?'] * 6

for row in data:
    x = row[:-1]
    if row[-1] == 'Yes':
        for i in range(6):
            if S[i] == '0':
                S[i] = x[i]
            elif S[i] != x[i]:
                S[i] = '?'
    else:
        for i in range(6):
            if S[i] != '?' and S[i] == x[i]:
                G[i] = '?'
            elif S[i] != '?' and S[i] != x[i]:
                G[i] = S[i]

print("Specific Boundary:", S)
print("General Boundary:", G)

plt.figure(figsize=(9, 4))
plt.axis('off')
table = plt.table(
    cellText=[S, G],
    rowLabels=['S Boundary', 'G Boundary'],
    colLabels=['Sky', 'AirTemp', 'Humidity',
               'Wind', 'Water', 'Forecast'],
    loc='center',
    cellLoc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 2)

plt.title("Candidate Elimination Boundaries")
plt.savefig("Exp-2-Output.png")
plt.show()
