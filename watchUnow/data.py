class Dane:
    name = ""
    tekst = ""

    def __init__(self, name, tekst):
        self.tekst = tekst
        self.name = name

    def getName(self):
        return self.name

    def getTekst(self):
        return self.tekst

    def setText(self, text):
        self.tekst = text

    def setName(self, name):
        self.name = name


class model(object):
    list1 = []
    # list1.append(Dane('Jot', 'Jokr fsd f sg gfsdg dgf sd'))