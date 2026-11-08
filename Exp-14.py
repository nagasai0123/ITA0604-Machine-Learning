
import matplotlib.pyplot as plt

area = [800, 1000, 1200, 1500, 1800, 2000]
price = [20, 25, 30, 38, 45, 50]

n = len(area)
mean_x = sum(area) / n
mean_y = sum(price) / n

m = sum((area[i] - mean_x) * (price[i] - mean_y)
        for i in range(n)) / sum((x - mean_x) ** 2 for x in area)

c = mean_y - m * mean_x

test = 1600
prediction = m * test + c

print("House Area:", test, "sq.ft")
print("Predicted Price:", round(prediction, 2), "Lakhs")

predictions = [m * x + c for x in area]

plt.scatter(area, price, label="Actual Prices")
plt.plot(area, predictions, label="Regression Line")
plt.scatter(test, prediction, color='red',
            label="Predicted Price")
plt.xlabel("Area (sq.ft)")
plt.ylabel("Price (Lakhs)")
plt.title("House Price Prediction")
plt.legend()
plt.savefig("Exp-14-Output.png")
plt.show()
