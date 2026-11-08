
import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6, 7, 8]
sales = [100, 120, 130, 150, 170, 180, 200, 220]

n = len(months)
mean_x = sum(months) / n
mean_y = sum(sales) / n

m = sum((months[i] - mean_x) * (sales[i] - mean_y)
        for i in range(n)) / sum((x - mean_x) ** 2 for x in months)

c = mean_y - m * mean_x

future_months = [9, 10, 11, 12]
predictions = [m * x + c for x in future_months]

print("Future Sales Prediction:")
for month, prediction in zip(future_months, predictions):
    print("Month", month, ":", round(prediction, 2))

all_months = months + future_months
all_sales = sales + predictions

plt.scatter(months, sales, label="Actual Sales")
plt.plot(all_months, all_sales, 'r--',
         label="Predicted Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Future Sales Prediction using Linear Regression")
plt.legend()
plt.savefig("Exp-20-Output.png")
plt.show()
