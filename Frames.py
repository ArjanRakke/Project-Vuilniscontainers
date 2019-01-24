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
        values = [0, 0, 0, 0, 0, 0, 0]
        values = self.calculate_values(controller)

        ax.bar(days, values)
        ax.set_facecolor('xkcd:white')
        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().grid()

    @staticmethod
    def calculate_values(cont):
        print('Totale omwonenden: {}'.format(cont.database('omwonende')))
        omwonenden = cont.database('omwonende')
        values = [0, 0, 0, 0, 0, 0, 0]
        for x in omwonenden:
            x_days = x[4]
            y_values = x[3]
            while len(x_days) > 0:
                if y_values > 1:
                    y_values -= 1
                if x_days[-2:] == 'ma':
                    values[0] += y_values
                if x_days[-2:] == 'di':
                    values[1] += y_values
                if x_days[-2:] == 'wo':
                    values[2] += y_values
                if x_days[-2:] == 'do':
                    values[3] += y_values
                if x_days[-2:] == 'vr':
                    values[4] += y_values
                if x_days[-2:] == 'za':
                    values[5] += y_values
                if x_days[-2:] == 'zo':
                    values[6] += y_values
                x_days = x_days[:-2]

        print('ma: {}\ndi: {}\nwo: {}\ndo: {}\nvr: {}\nza: {}\nzo: {}'.format(values[0], values[1], values[2], values[3], values[4], values[5], values[6]))
        return values



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
