import tkinter as gui
from matplotlib import style
style.use("ggplot")

# Declare some fonts and variables
titleFont = ("Arial Rounded MT Bold", 20)
smallFont = ("console", 9)
mediumFont = ("console", 12)


# Empty frame for testing
class EmptyFrame(gui.Frame):
    def __init__(self, master, controller):
        gui.Frame.__init__(self, master)
        self.label = gui.Label(self, text='Empty').grid()


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



