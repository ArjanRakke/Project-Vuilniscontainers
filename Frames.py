import tkinter as gui
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
style.use('ggplot')

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

        f = Figure(figsize=(10, 5), dpi=100)
        ax = f.add_subplot(111)


# CONTAINER FRAMES
# How full & basic data
# Emptying Data

class ContainerGraphFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Graph').grid()


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
