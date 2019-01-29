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
        print('Totale omwonenden: {}'.format(cont.database_query('omwonende')))
        omwonenden = cont.database_query('omwonende')
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

        self.background_image = gui.PhotoImage(file='resources/template.gif')
        self.background_label = gui.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.background_label.photo = self.background_image
        self.label = gui.Label(self, text="VUILOPHAALDIENST", bg="#FFF", font=titleFont, fg="#056d00")
        self.label.place(x=124, y=100)

        # self.drop_down_default = gui.StringVar(self)
        # self.drop_down_default.set(self.current_container[1])
        # drop_down = gui.OptionMenu(self, self.drop_down_default, *self.all_containers, command=self.update_vars)

        self.button_graph = gui.Button(self, text='Vuilnis/Dag', command=lambda: controller.generate_graph('UMC'),
                                       bg="#E16A27", fg="black", relief="flat", activebackground="#bc4505", activeforeground="white",
                                       cursor="hand2", font=mediumFont)
        self.button_graph.place(x=173, y=200, width=127, height=50)


class PickContainerFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)

        # Background
        self.bg_img = gui.PhotoImage(file='resources/template.gif')
        self.bg_label = gui.Label(self, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.photo = self.bg_img

        # Title
        self.title = gui.Label(self, text="UTRECHT AFVALDIENST", font=titleFont, bg="#FFF", fg="#056d00",)
        self.title.place(x=124, y=100)

        # Dropdown
        self.dropdown_default = gui.StringVar(self)
        self.dropdown_default.set(controller.current_container.get())
        self.dropdown = gui.OptionMenu(self, controller.current_container, *controller.all_containers, command=controller.next_container)
        self.dropdown.place(x=173, y=200, width=127, height=50)

        self.button_graph = gui.Button(self, text='Vuilnis/Dag', command=lambda: controller.generate_graph(controller.current_container.get()),
                                       bg="#E16A27", fg="black", relief="flat", activebackground="#bc4505", activeforeground="white",
                                       cursor="hand2", font=mediumFont)
        self.button_graph.place(x=173, y=250, width=127, height=50)



