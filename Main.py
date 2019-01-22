import tkinter as gui
import tkinter.messagebox
from Frames import EmptyFrame, ContainerDataFrame, ContainerEmptyFrame, SettingsFrame, GraphFrame


class MainApplication(gui.Tk):
    def __init__(self, *args, **kwargs):
        gui.Tk.__init__(self, *args, **kwargs)

        # Toolbar
        toolbar = gui.Frame(self, bd=1, relief='raised')
        toolbar.pack(side='top', fill='x')

        # Container contains everything
        container = gui.Frame(self)
        container.pack(fill='x')

        #self.geometry('768x432')
        self.frames = {}

        # Initializes frames with [container] as master and [self] as controller
        for F in (EmptyFrame, ContainerDataFrame, ContainerEmptyFrame, SettingsFrame, GraphFrame):
            self.frames[F] = F(container, self)
            self.frames[F].grid(row=0, sticky='news')
        self.show_frame(ContainerEmptyFrame)

        button_container_empty = gui.Button(toolbar, text='Container Emptying', command=lambda: self.show_frame(ContainerEmptyFrame))
        button_container_data = gui.Button(toolbar, text='Container Data', command=lambda: self.show_frame(ContainerDataFrame))
        button_settings = gui.Button(toolbar, text='Settings', command=lambda: self.show_frame(SettingsFrame))
        button_graph = gui.Button(toolbar, text='Graph', command=lambda: self.show_frame(GraphFrame))
        button_empty = gui.Button(toolbar, text='Empty', command=lambda: self.show_frame(EmptyFrame))

        button_container_empty.pack(side='left', padx=2, pady=2)
        button_container_data.pack(side='left', padx=2, pady=2)
        button_settings.pack(side='left', padx=2, pady=2)
        button_graph.pack(side='left', padx=2, pady=2)
        button_empty.pack(side='left', padx=2, pady=2)

    # Show specific frame
    def show_frame(self, cont):
        self.frames[cont].tkraise()

    # Pop up messages
    @staticmethod
    def message_box(type_message, message):
        if type_message == 'info':
            gui.messagebox.showinfo('Info', message)
        if type_message == 'error':
            gui.messagebox.showerror('Error', message)
        if type_message == 'warning':
            gui.messagebox.showwarning('Warning', message)

    # Gets data from database
    @staticmethod
    def database():
        return None


app = MainApplication()
app.mainloop()
