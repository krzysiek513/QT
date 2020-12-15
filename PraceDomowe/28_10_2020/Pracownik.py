class Error(Exception):
    """Base class for other exceptions"""
    pass


class WrongOption(Error):
    """Za duzo"""
    pass


class Pracownik:
    # Zmienne
    imie = ""
    nazwisko = ""
    stanowisko = ""
    nrPracownika = None
    wyplata = 0.0

    def __init__(self, imie=None, nazwisko=None, stanowisko="Prezes", nrPracownika=1, wyplata=None):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self.nrPracownika = nrPracownika
        self.wyplata = wyplata

    def __str__(self):
        if(self.nrPracownika==1):
            return 'Prezes - Imie: {s.imie} | nazwisko: {s.nazwisko} | stanowisko: {s.stanowisko} | ' \
                   'nrPracownika: {s.nrPracownika}'.format(
                s=self)
        else:
            return 'Pracownik - Imie: {s.imie} | nazwisko: {s.nazwisko} | stanowisko: {s.stanowisko} | ' \
                   'nrPracownika: {s.nrPracownika}'.format(
                s=self)

    def przydzielNr(self, nr):
        if nr > 0:
            print(f"Nowy nr pracownika {self.imie} {self.nazwisko} to {nr}")
            self.nrPracownika = nr
        else:
            print("Podaleś zły nr")

    def podwyzka(self, wartosc):
        print(f'Aktualna wypłata: {self.wyplata}')
        try:
            if self.nrPracownika == 1:
                self.wyplata += wartosc + 200
            elif wartosc > 300:
                raise WrongOption
            else:
                self.wyplata += wartosc
        except WrongOption:
            print("nie udało się podnieść wypłaty")
        print(f'Wypłata po podniesieniu wartosci: {self.wyplata}')
