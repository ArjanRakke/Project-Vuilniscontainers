import tkinter as gui
from matplotlib import style
style.use("ggplot")

# Declare some fonts and variables
titleFont = ("Arial Rounded MT Bold", 20)
titleFont2 = ("Arial Unicode MS", 20)
smallFont = ("console", 9)
mediumFont = ("console", 12)


# Empty frame for testing
class EmptyFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Empty').grid()


# The main frame, with all included controls
class PickContainerFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)

        # Background
        self.bg_img = gui.PhotoImage(file='resources/background5.gif')
        self.bg_label = gui.Label(self, image=self.bg_img)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.photo = self.bg_img

        # Title
        self.title1 = gui.Label(self, text="UTRECHT", font=titleFont2, bg="#FFF", fg="#056d00",)
        self.title1.place(x=150, y=50)

        self.title2 = gui.Label(self, text="AFVALDIENST", font=titleFont, bg="#FFF", fg="#056d00",)
        self.title2.place(x=120, y=20)

        # Info
        # self.label_location = gui.Label(self, textvariable=controller.current_container, bg="#FFF", fg="#056d00")
        # self.label_location.place(x=200, y=180)

        # Dropdown
        self.dropdown_default = gui.StringVar(self)
        self.dropdown_default.set(controller.current_container.get())
        self.dropdown = gui.OptionMenu(self, controller.current_container, *controller.all_containers, command=controller.next_container)
        self.dropdown.place(x=96, y=116, width=259, height=60)

        # Button
        self.button_graph = gui.Button(self, text='Vuilnis/Dag', command=lambda: controller.generate_graph(controller.current_container.get()),
                                       bg="#eea200", fg="black", relief="flat", activebackground="#b15902", activeforeground="white",
                                       cursor="hand2", font=mediumFont)
        self.button_graph.place(x=85, y=250, width=280, height=53)
