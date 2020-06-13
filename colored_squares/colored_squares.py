
import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x*x for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, s=3)

ax.set_title('Squares of numbers', fontsize=24)
ax.set_xlabel('Numbers', fontsize=14)
ax.set_ylabel('Squares', fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

ax.axis([0, 5100, 0, 26_000_000])

#plt.savefig('colored_squares.png')
plt.show()