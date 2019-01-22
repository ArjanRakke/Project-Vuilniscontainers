import matplotlib.pyplot as plt

kilo_afval = [10, 22, 80, 60, 23, 60, 75]
dag = ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"]

plt.bar(dag, kilo_afval)

plt.xlabel("dag")
plt.ylabel("kilo afval")
plt.title("placeholder")
plt.legend()
plt.show()
