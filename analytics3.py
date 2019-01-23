import tkinter as Tk
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
style.use('ggplot')

root = Tk.Tk()
root.title("afval storting per dag")

f = Figure(figsize=(10, 5), dpi=100)
ax = f.add_subplot(111)
ax.bar(("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag"), [20, 35, 30, 36, 27, 30, 25])

canvas = FigureCanvasTkAgg(f, root)
canvas.draw()
canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

Tk.mainloop()
