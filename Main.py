import tkinter as gui
import tkinter.messagebox
from Frames import EmptyFrame, ContainerDataFrame, ContainerGraphFrame, SettingsFrame, GraphFrame
import mysql.connector


class MainApplication(gui.Tk):
    def __init__(self, *args, **kwargs):
        gui.Tk.__init__(self, *args, **kwargs)

        # Toolbar
        toolbar = gui.Frame(self, bd=1, relief='raised')
        toolbar.pack(side='top', fill='x')

        # Container contains everything
        container = gui.Frame(self)
        container.pack(fill='x')

        self.frames = {}
        # self.data = self.database()
        # self.current_container = self.data[0]
        self.data = ()
        self.current_container = []

        self.ID_var = gui.IntVar()
        self.location_var = gui.StringVar()
        self.room_var = gui.IntVar()
        self.total_room = gui.IntVar()

        self.update_vars(0)

        # Initializes frames with [container] as master and [self] as controller
        # All frames are piled up, show_frame puts a specific frame on top
        for F in (EmptyFrame, ContainerDataFrame, ContainerGraphFrame, SettingsFrame, GraphFrame):
            self.frames[F] = F(container, self)
            self.frames[F].grid(row=0, sticky='news')
        self.show_frame(ContainerGraphFrame)

        button_container_empty = gui.Button(toolbar, text='Dagelijkse Vuilnis', command=lambda: self.show_frame(ContainerGraphFrame))
        button_container_data = gui.Button(toolbar, text='Container Data', command=lambda: self.show_frame(ContainerDataFrame))
        button_settings = gui.Button(toolbar, text='Settings', command=lambda: self.show_frame(SettingsFrame))
        button_graph = gui.Button(toolbar, text='Graph', command=lambda: self.show_frame(GraphFrame))
        button_refresh = gui.Button(toolbar, text='Refresh', command=lambda: self.database())

        self.drop_down_default = gui.StringVar(self)
        self.drop_down_default.set(self.current_container[1])
        drop_down = gui.OptionMenu(toolbar, self.drop_down_default, self.data[0][1])

        button_container_empty.pack(side='left', padx=2, pady=2)
        button_container_data.pack(side='left', padx=2, pady=2)
        button_settings.pack(side='left', padx=2, pady=2)
        button_graph.pack(side='left', padx=2, pady=2)
        button_refresh.pack(side='left', padx=2, pady=2)
        drop_down.pack(side='right', padx=2, pady=2)

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
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="project_vuilnis"
        )
        cmd = db.cursor()
        cmd.execute("SELECT * FROM containers")
        result = cmd.fetchall()
        return result

    def update_vars(self, id):
        self.data = self.database()
        self.current_container = self.data[id]

        self.ID_var.set(self.current_container[0])
        self.location_var.set(self.current_container[1])
        self.room_var.set(self.current_container[2])
        self.total_room.set(self.current_container[3])

        print('Current: {}'.format(self.current_container))


app = MainApplication()
app.mainloop()
