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

        # The frames contain specific elements, and will be displayed in [container]
        # Data contains all data from the database
        self.frames = {}
        self.data = ()
        self.current_container = []

        # Every container has these variables, which are updated based on the [self.current_container]
        # The current container is the top row in the database by default
        self.ID_var = gui.IntVar()
        self.location_var = gui.StringVar()
        self.room_var = gui.IntVar()
        self.total_room = gui.IntVar()
        self.update_vars()

        # All container locations in a list, for the drop down menu
        self.all_containers = []
        for x in self.data:
            self.all_containers.append(x[1])

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

        # self.drop_down_default = gui.StringVar(self)
        # self.drop_down_default.set(self.current_container[1])
        # drop_down = gui.OptionMenu(toolbar, self.drop_down_default, *self.all_containers, command=self.update_vars)

        button_container_empty.pack(side='left', padx=2, pady=2)
        button_container_data.pack(side='left', padx=2, pady=2)
        button_settings.pack(side='left', padx=2, pady=2)
        button_graph.pack(side='left', padx=2, pady=2)
        button_refresh.pack(side='left', padx=2, pady=2)
        # drop_down.pack(side='right', padx=2, pady=2)

    # Show specific frame
    def show_frame(self, cont):
        self.frames[cont].tkraise()

    # Gets data from database
    @staticmethod
    def database(table):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="database_vuilophaaldienst"
            )
            cmd = db.cursor()

            if table == 'containers':
                cmd.execute("SELECT * FROM containers")
            if table == 'omwonende':
                cmd.execute("SELECT * FROM omwonende")
            result = cmd.fetchall()
            return result
        except:
            gui.messagebox.showerror("Foutmelding", "Er kon geen verbinding gemaakt worden met de database.")

    def update_vars(self):
        self.data = self.database('containers')
        self.current_container = self.data[0]

        self.ID_var.set(self.current_container[0])
        self.location_var.set(self.current_container[1])
        self.room_var.set(self.current_container[2])
        self.total_room.set(self.current_container[3])

        print('Current container: {}'.format(self.current_container))

    @staticmethod
    def tester(thing):
        print(thing)


app = MainApplication()
app.mainloop()
