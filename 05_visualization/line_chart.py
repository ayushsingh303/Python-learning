# Python Data Visualization
import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
study_hours = [2, 3, 4, 3, 5]

plt.plot(days, study_hours, marker="o")

plt.title("My Weekly Study Hours")
plt.xlabel("Day")
plt.ylabel("Study Hours")

plt.show()
