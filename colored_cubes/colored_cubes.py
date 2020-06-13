
import matplotlib.pyplot as plt

x_values = range(0, 5001)
y_vaules = [x*x*x for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
plt.scatter(x_values, y_vaules, c=y_vaules, cmap=plt.cm.cool, s=3)

ax.set_title("Cubes of Numbers", fontsize=24)
ax.set_xlabel("Numbers", fontsize=14)
ax.set_ylabel("Cubes", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

ax.axis([0, 5100, 0, 130000000000])

#plt.savefig("colored_cubes.png")
plt.show()
