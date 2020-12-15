import Pracownik

if __name__ == '__main__':
    asdf = Pracownik.Pracownik(imie="Krzysiek", nazwisko="Jot", wyplata=11111)

listaPracownikow = [asdf]
nowy2 = Pracownik.Pracownik(imie="Barbara", nazwisko="Kotecka", stanowisko="Sekretrka", nrPracownika=2, wyplata=4444)
listaPracownikow.append(nowy2)
nowy3 = Pracownik.Pracownik(imie="Hania", nazwisko="Chłopińska", stanowisko="Asystent", nrPracownika=3, wyplata=2222)
listaPracownikow.append(nowy3)

print("\n")
nie = None
while nie != "nie":
    print("Dodaj nowego pracownika (dodaj)")
    print("Pokaż pracowników (pokaż) ")
    print("Daj podwyżke (kasa) ")
    print("Usunąć pracownika (usuń) ")
    print("wyjdź (nie) ")
    nie = input("Co zrobić? ")
    if nie == "dodaj":
        imie = input("Imie ")
        nazwisko = input("Nazwisko ")
        nrPracownika = input("Numer ")
        stanowsko = input("Stanowisko ")
        kasa = input("Jaka ma wypłate ")
        nowy4 = Pracownik.Pracownik(imie=imie, nazwisko=nazwisko, stanowisko=stanowsko,
                                    nrPracownika=nrPracownika, wyplata=kasa)
        listaPracownikow.append(nowy4)

    elif nie == "pokaż":
        for i in listaPracownikow:
            print(i)
    elif nie == "kasa":
        hajs = int(input("Ile pieniędzy chcesz mu dać? "))
        numer = int(input("Podaj numer pracownika "))
        for i in listaPracownikow:
            if numer == i.nrPracownika:
                i.podwyzka(hajs)
    elif nie == "usuń":
        numer = int(input("Posaj numer pracownika do usunięcia "))
        for i in listaPracownikow:
            if numer == i.nrPracownika:
                listaPracownikow.remove(i)
    elif nie == "nie":
        print("Do zobaczenia")
    else:
        print("zły wbór!")
    print("\n")
