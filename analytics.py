import matplotlib.pyplot as plt
import random as r

mensen = r.sample(range(131), 30)
ids = [x for x in range(len(mensen))]

plt.bar(ids, mensen)

plt.xlabel("x")
plt.ylabel("y")
plt.title("placeholder")
plt.legend()
plt.show()
