class Student:
    nick = ""
    name = ""
    lastName = ""

    def __init__(self, lastName, name, nick):
        self.nick = nick
        self.lastName = lastName
        self.name = name

    def getLastname(self):
        return self.lastName

    def getName(self):
        return self.name

    def getNick(self):
        return self.nick


class model1(object):
    list1 = []
    list1.append(Student('Krzysiek', 'Jot', 'Jokr'))
    list1.append(Student('Replika', 'Jot', 'Jore'))
