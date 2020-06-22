
import matplotlib.pyplot as plt

xx_values = range(0, 126)
xxx_values = range(0, 26)

yy_values = [x*x for x in xx_values]
yyy_values = [x*x*x for x in xxx_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
plt.plot(xx_values, yy_values, c="green", linewidth=3)
plt.plot(xxx_values, yyy_values, c="yellow", linewidth=3)

ax.set_title("Comparing Squares and Cubes of Numbers", fontsize=24)
ax.set_xlabel("Numbers", fontsize=14)
ax.set_ylabel("Squares and Cubes", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

ax.axis([0, 130, 0, 17000])

plt.savefig("comparison.png")
plt.show()