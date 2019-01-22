import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

afval_storting = {"dag": ["maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"],
                  "kilos_afval": [5, 7, 4, 8, 6, 12, 9]}

df = pd.DataFrame(afval_storting)
df.set_index("dag", inplace=True)

plt.bar(afval_storting["dag"], afval_storting["kilos_afval"])

plt.xlabel("dag")
plt.ylabel("kilo afval")
plt.title("placeholder")
plt.show()
print(df)
