import tkinter as gui
import tkinter.messagebox
from Frames import EmptyFrame, ContainerDataFrame
import mysql.connector

####################################
# REMEMBER TO REMOVE UNUSED FRAMES #
####################################

# f0ffef = groen

class MainApplication(gui.Tk):
    def __init__(self, *args, **kwargs):
        gui.Tk.__init__(self, *args, **kwargs)
        # Contains all other frames
        box = gui.Frame(self)
        box.place(x=0, y=0, width=768, height=432)
        box.grid_rowconfigure(0, weight=1)
        box.grid_columnconfigure(0, weight=1)

        self.current_container = gui.StringVar()
        self.update_vars(self)

        # Each frame is defined in Frames.py, and contains a specific set of controls
        self.frames = {}
        for F in (EmptyFrame, ContainerDataFrame):
            self.frames[F] = F(box, self)
            self.frames[F].grid(row=0, column=0, sticky='news')
        self.show_frame(ContainerDataFrame)

    def show_frame(self, controller):
        self.frames[controller].tkraise()

    def message_box(self, title, message, message_type):
        if message_type == "info":
            gui.messagebox.showinfo(title, message)
        elif message_type == "warning":
            gui.messagebox.showwarning(title, message)
        else:
            gui.messagebox.showerror(title, message)

    def database(self):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='database_vuilophaaldienst'
        )
        cmd = db.cursor()
        cmd.execute('SELECT * FROM containers')
        result = cmd.fetchall()

        print('Database: {}'.format(result))
        return result

    def update_vars(self, controller):
        result = self.database()
        controller.current_container.set(result[0][1])


    @staticmethod
    def test(test):
        print(test)




""""
        # Container contains everything
        container = gui.Frame(self)
        container.pack(fill='x')

        # The frames contain specific elements, and will be displayed in [container]
        # Data contains all data from the database
        self.frames = {}
        self.container_data = ()
        self.current_container = []

        # Every container has these variables, which are updated based on the [self.current_container]
        # The current container is the top row in the database by default
        self.ID_var = gui.IntVar()
        self.location_var = gui.StringVar()
        self.room_var = gui.IntVar()
        self.total_room = gui.IntVar()
        self.update_vars()

        self.geometry = ""

        # All container locations in a list, for the drop down menu
        self.all_containers = []
        for x in self.container_data:
            self.all_containers.append(x[1])

        # Initializes frames with [container] as master and [self] as controller
        # All frames are piled up, show_frame puts a specific frame on top
        for F in (EmptyFrame, ContainerDataFrame, ContainerGraphFrame, SettingsFrame, GraphFrame):
            self.frames[F] = F(container, self)
            self.frames[F].grid(row=0, sticky='news')
        self.show_frame(ContainerGraphFrame)

        self.drop_down_default = gui.StringVar(self)
        self.drop_down_default.set(self.current_container[1])

    # Show specific frame
    def show_frame(self, cont):
        self.frames[cont].tkraise()

    # Gets data from database
    @staticmethod
    def database(table, loc=None):
        try:
            db = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="",
                database="database_vuilophaaldienst"
            )
            cmd = db.cursor()

            if table == 'containers':
                # If no location is specified all locations will be fetched
                if loc != None:
                    query = "SELECT * FROM `containers` WHERE `locatie` = '{}'".format(loc)
                    cmd.execute(query)
                else:
                    cmd.execute("SELECT * FROM containers")
            if table == 'omwonende':
                cmd.execute("SELECT * FROM omwonende")
            result = cmd.fetchall()
            return result
        except:
            gui.messagebox.showerror("Foutmelding", "Er kon geen verbinding gemaakt worden met de database.")

    def update_vars(self, loc=None):
        self.container_data = self.database('containers', loc)
        self.current_container = self.container_data[0]

        self.ID_var.set(self.current_container[0])
        self.location_var.set(self.current_container[1])
        self.room_var.set(self.current_container[2])
        self.total_room.set(self.current_container[3])
        print('Current container: {}'.format(self.current_container))

        self.people_data = self.database('omwonende')
        self.days = ('maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag')
        self.daily_trash = [0, 0, 0, 0, 0, 0, 0]

        for x in self.people_data:
            self.value = x[3]
            self.day = x[4]
            while (len(self.day) > 0):
                if self.value > 1:
                    self.value -= 1
                if self.day[-2:] == 'ma':
                    self.daily_trash[0] += self.value
                if self.day[-2:] == 'di':
                    self.daily_trash[1] += self.value
                if self.day[-2:] == 'wo':
                    self.daily_trash[2] += self.value
                if self.day[-2:] == 'do':
                    self.daily_trash[3] += self.value
                if self.day[-2:] == 'vr':
                    self.daily_trash[4] += self.value
                if self.day[-2:] == 'za':
                    self.daily_trash[5] += self.value
                if self.day[-2:] == 'zo':
                    self.daily_trash[6] += self.value
                self.day = self.day[:-2]
        print('trash: {}'.format(self.daily_trash))

        return self.daily_trash




    @staticmethod
    def tester(thing):
        print(thing)

"""

app = MainApplication()
# nsFietsenStalling.iconbitmap('resources/favicon.ico')
app.geometry("768x432")
app.title("Container Manager")

app.mainloop()