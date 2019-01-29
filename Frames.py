import tkinter as gui
import tkinter.messagebox
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import datetime
import re

# Declare some fonts and variables
titleFont = ("Arial Rounded MT Bold", 20)
smallFont = ("console", 9)
mediumFont = ("console", 12)
buttonOptions = ()


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

        background_image = gui.PhotoImage(file='resources/background.gif')
        background_label = gui.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.photo = background_image
        label = gui.Label(self, text="VUILOPHAALDIENST UTRECHT", bg="#FFF", font=titleFont, fg="#056d00")
        label.place(x=124, y=100)

        # self.button = gui.Button(self, text='Vuilnis/Dag', command=lambda: self.check_container(controller))
        # self.button.pack()

    def check_container(self, controller):
        result = controller.database()

        days = ['ma', 'di', 'wo', 'do', 'vr', 'za', 'zo']
        trash = [4, 0, 1, 0, 4, 2, 0]

        afval_storting = {"dag": days,
                          "Vuilniszakken": trash}
        liters_afval = [x * 60 for x in afval_storting["Vuilniszakken"]]

        df = pd.DataFrame(afval_storting)
        df.set_index("dag", inplace=True)

        plt.bar(afval_storting["dag"], liters_afval)
        plt.xlabel("Dag")
        plt.ylabel("Liter")
        plt.title("Afval in Liters/Dag")
        plt.show()
        print(df)
