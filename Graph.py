import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

afval_storting = {"dag": ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"],
                  "Vuilniszakken": [4, 0, 1, 0, 4, 2, 0]}

liters_afval = [x * 60 for x in afval_storting["vuilniszakken"]]

df = pd.DataFrame(afval_storting)
df.set_index("dag", inplace=True)

plt.bar(afval_storting["dag"], liters_afval)

plt.xlabel("Dag")
plt.ylabel("Liter")
plt.title("Afval in Liters/Dag")
plt.show()
print(df)