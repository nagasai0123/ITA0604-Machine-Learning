
import matplotlib.pyplot as plt

mileage = [10, 20, 30, 40, 50, 60]
price = [9, 8, 7, 6, 5, 4]

n = len(mileage)
mean_x = sum(mileage) / n
mean_y = sum(price) / n

m = sum((mileage[i] - mean_x) * (price[i] - mean_y)
        for i in range(n)) / sum((x - mean_x) ** 2 for x in mileage)

c = mean_y - m * mean_x

test = 35
predicted_price = m * test + c

print("Mileage:", test, "km/l")
print("Predicted Price:", round(predicted_price, 2), "Lakhs")

predictions = [m * x + c for x in mileage]

plt.scatter(mileage, price, label="Actual Prices")
plt.plot(mileage, predictions, label="Regression Line")
plt.scatter(test, predicted_price, color='red',
            label="Predicted Price")
plt.xlabel("Mileage (km/l)")
plt.ylabel("Price (Lakhs)")
plt.title("Car Price Prediction")
plt.legend()
plt.savefig("Exp-13-Output.png")
plt.show()
