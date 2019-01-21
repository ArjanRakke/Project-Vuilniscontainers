from tkinter import *
from Frames import EmptyFrame, ContainerFrame


class MainApplication(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        container = Frame(self)
        container.grid()

        self.grid_rowconfigure(0, weight=1)
        self.frames = {}

        for F in (EmptyFrame, ContainerFrame):
            self.frames[F] = F(container, self)
            self.frames[F].grid(row=0, column=0, sticky='news')
        self.show_frame(ContainerFrame)

    def show_frame(self, cont):
        self.frames[cont].tkraise()


app = MainApplication()
app.mainloop()