class Student:
    def __init__(self, data):
        data = data.split(' ')
        self.last_name = data[0]
        self.name = data[1]
        self.points = int(data[2]) + int(data[3]) + int(data[4])

    def to_string(self):
        return self.last_name + " " + self.name
