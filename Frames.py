from tkinter import *
# from PIL import Image, ImageTk


class EmptyFrame(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.button = Button(self, text='EmptyFrame', command=lambda: controller.show_frame(ContainerFrame))
        self.button.grid(row=0, column=0)


class ContainerFrame(Frame):
    def __init__(self, master, controller):
        Frame.__init__(self, master)
        self.button = Button(self, text='ContainerFrame', command=lambda: controller.show_frame(EmptyFrame))
        self.button.grid(row=0, column=0)

        # img = ImageTk.PhotoImage(Image.open('Project/container_empty.png'))
        # self.label = Label(self, image=img)
        # self.label.image = img
        # self.label.grid()
