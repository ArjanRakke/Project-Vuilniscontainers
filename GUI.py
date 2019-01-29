import tkinter as gui
from Frames import EmptyFrame, ContainerDataFrame, PickContainerFrame
import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")

####################################
# REMEMBER TO REMOVE UNUSED FRAMES #
####################################

# f0ffef = groen
# E16A27 = geel

class MainApplication(gui.Tk):
    def __init__(self, *args, **kwargs):
        gui.Tk.__init__(self, *args, **kwargs)
        # Contains all other frames
        box = gui.Frame(self)
        box.place(x=0, y=0, width=768, height=432)
        box.grid_rowconfigure(0, weight=1)
        box.grid_columnconfigure(0, weight=1)

        self.current_container = gui.StringVar()
        self.all_containers = self.get_containers()
        self.current_container.set(self.all_containers[0])

        # Each frame is defined in Frames.py, and contains a specific set of controls
        self.frames = {}
        for F in (EmptyFrame, ContainerDataFrame, PickContainerFrame):
            self.frames[F] = F(box, self)
            self.frames[F].grid(row=0, column=0, sticky='news')
        self.show_frame(PickContainerFrame)

    def show_frame(self, controller):
        self.frames[controller].tkraise()

    # Executes whatever injected query
    @staticmethod
    def database_query(query):
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='database_vuilophaaldienst'
        )
        cmd = db.cursor()
        cmd.execute(query)
        result = cmd.fetchall()

        # print('Query: {}\nResult: {}\n'.format(query, result))
        return result

    # Get all containers by name, and put them in a list
    def get_containers(self):
        container_data = self.database_query("SELECT `locatie` FROM `containers`")
        return container_data

    # Generate and show graph
    def generate_graph(self, container):
        # Unknown which container each person uses
        # If this becomes known just add "WHERE 'location' = '{}'".format(container) to the query
        monday = 0
        tuesday = 0
        wednesday = 0
        thursday = 0
        friday = 0
        saturday = 0
        sunday = 0

        for x in self.database_query("SELECT `vuilniszakken_per_week` FROM `omwonende` WHERE `dag_van_storting` = 'maandag'"):
            monday += x[0]
        for x in self.database_query("SELECT `vuilniszakken_per_week` FROM `omwonende` WHERE `dag_van_storting` = 'dinsdag'"):
            tuesday += x[0]
        for x in self.database_query("SELECT `vuilniszakken_per_week` FROM `omwonende` WHERE `dag_van_storting` = 'woensdag'"):
            wednesday += x[0]
        for x in self.database_query("SELECT `vuilniszakken_per_week` FROM `omwonende` WHERE `dag_van_storting` = 'donderdag'"):
            thursday += x[0]
        for x in self.database_query("SELECT `vuilniszakken_per_week` FROM `omwonende` WHERE `dag_van_storting` = 'vrijdag'"):
            friday += x[0]
        for x in self.database_query("SELECT `vuilniszakken_per_week` FROM `omwonende` WHERE `dag_van_storting` = 'zaterdag'"):
            saturday += x[0]
        for x in self.database_query("SELECT `vuilniszakken_per_week` FROM `omwonende` WHERE `dag_van_storting` = 'zondag'"):
            sunday += x[0]

        days = ['ma', 'di', 'wo', 'do', 'vr', 'za', 'zo']
        trash = [monday, tuesday, wednesday, thursday, friday, saturday, sunday]
        print(self.current_container.get())

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

    # Assigns specific container to 'self.current_container'
    def next_container(self, container):
        self.current_container.set(container)

    # Does nothing, used for testing
    @staticmethod
    def test(test):
        # db = Database(test)
        # print(db.execute_query())
        print('Nothing')


app = MainApplication()
# app.iconbitmap('resources/favicon.ico')
app.geometry("768x432")
app.title("Container Manager")

app.mainloop()