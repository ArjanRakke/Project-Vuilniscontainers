import mysql.connector

# INPUT
# How much trash fits in the container
# How often people throw trash in the container
# How many bags of trash people usually throw in the container

# PROCESS
# 24 hours in a day
# During which of these hours is the container 80%+ full?

# OUTPUT
# Time for emptying (1 or more)


def check_room(room, total_room):
    room_percentage = (room / total_room) * 100
    if room_percentage > 80:
        print('vol')
    else:
        print('nog ruimte over')


check_room(25, 30)


class Container:
    def __init__(self):
        self.room = 30
        self.total_room = 35
        self.location = 'UMC'












# VARIABLES AND PROPERTIES
# container_bags = 25
# trash_per_person = 2
# times_person_adds_trash = 1

# containers = database()

# for x in result:
#     print(x)


""""
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


# containers = database()
# Location = containers[-][1]
# Current Room = containers[-][2]
# Total Room = containers[-][3]


def algorithm(containers):

    return None


class Containerssssss(object):
    def __init__(self, container):
        self.containers = self.database()
        self.location

    @staticmethod
    def database():
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='project_vuilnis'
        )
        cmd = db.cursor()
        cmd.execute('SELECT * FROM containers')
        result = cmd.fetchall()
        return result


containers = database()
for x in containers:


class Container(object):
    def __init__(self, data):
        self.Location = data[1]
        print(self.Location)

"""