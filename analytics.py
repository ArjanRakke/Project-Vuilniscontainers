import matplotlib.pyplot as plt

mensenLeeftijd = [10, 22, 80, 60, 23, 60, 75, 87, 24, 67, 13, 56, 79, 47]
ids = [x for x in range(len(mensenLeeftijd))]

plt.bar(ids, mensenLeeftijd)

plt.xlabel("x")
plt.ylabel("y")
plt.title("placeholder")
plt.legend()
plt.show()
