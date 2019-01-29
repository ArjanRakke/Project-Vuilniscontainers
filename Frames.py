import tkinter as gui
from matplotlib import style
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
style.use('ggplot')


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
        f = Figure(figsize=(10, 5), dpi=100)
        ax = f.add_subplot(111)

        days = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')
        values = controller.values

        ax.bar(days, values)
        ax.set_facecolor('xkcd:white')
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid()


class ContainerDataFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Container').grid()
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
