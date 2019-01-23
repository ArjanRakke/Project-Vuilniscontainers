import tkinter as gui
""""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import numpy as np
"""


# Empty frame for testing
class EmptyFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Empty').grid()


# CONTAINER FRAMES
# How full & basic data
# Emptying Data

class ContainerGraphFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Graph').grid()

        # self.label_number = gui.Label(self, textvariable=controller.number_var).grid()
        # self.label_location = gui.Label(self, textvariable=controller.location_var).grid()

        # self.trash = {"day": ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"],
        #  "trash_kilo": [5, 7, 4, 8, 6, 12, 9]}
        # fig = Figure(figsize=(5, 4), dpi=100)
        # t = np.arange(0, 3, .01)
        # fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

        # canvas = FigureCanvasTkAgg(fig, master=self)  # A tk.DrawingArea.
        # canvas.draw()
        # canvas.get_tk_widget().grid()
        # canvas.get_tk_widget().pack(side=gui.TOP, fill=gui.BOTH, expand=1)

        # df = pd.DataFrame(self.trash)
        # df.set_index("dag", inplace=True)

        # plt.bar(self.trash["dag"], self.trash["kilos_afval"])

        # plt.xlabel("dag")
        # plt.ylabel("kilo afval")
        # plt.title("placeholder")
        # plt.show()
        # print(df)


class ContainerDataFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Data').grid()
        self.label_location = gui.Label(self, text='Location').grid()
        self.label_percentage = gui.Label(self, text='Container at 0%')


# OTHER FRAMES
# Settings
# Graphs that concern all containers

class SettingsFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Settings').grid()


class GraphFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Graph').grid()


""""
# Every container gets a [Container Frame], displaying all important data
class ContainerFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.button = gui.Button(self, text='ContainerFrame', command=lambda: controller.show_frame(EmptyFrame))
        self.button.grid(row=0, column=0)

        # Container % filled up
        # Container name
        # Container location
        # Last time emptied


class MenuFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)

        self.button_exit = gui.Button(self, text='Exit', command=lambda: self.exit_this())
        self.button_exit.grid()

    def exit_this(self):
        sys.exit(0)

        # Graph
        # Basic Info
        # Empty
        # Exit
        # Next

"""
