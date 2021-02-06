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
    bug = 'Aplikacja ma służyć dla nas jako notatik. \n' \
          'Ma na celu gromadzenie danych tekstowych zapisanych pod określoną nazwą\n' \
          ' Na aplikacje składa się pasek menu posiadający rózne funkcje.\n' \
          ' Po lewno mamy pole wyboru interesującego nas zagadnienia.\n' \
          ' Po prawo many pole które wyświetla dane na temat naszego zagadnienia\n\n' \
          'Użycie aplikacji:\n' \
          '     pasek menu\n' \
          'Znajduje się on na górze aplikacji i składa się z sześciu rozwijanych list' \
          'Pierwsza to file jest w niej klika opcji. NEW Tworzy nowy notatnik' \
          'Open - otwiera wcześniej zapisany notatnik, Save - opcja ta służy do zapisy notatek' \
          'Quit - służy do zamknięcia aplikacji\n' \
          'Drugą opcją jest edit - do zrobienia\n' \
          'potem jest View - zoomIm i zoomOut, służą odpowiednio do zwiększania i zmniejszania czcionki w wyświetlonym tekście\n' \
          'Search - do zrobienia\n' \
          'Tools - word count - zlicza ilość wyświetlonego tekstu w dokładności do znaku\n' \
          'Na końcu znajduje się help. W tym dziale mamy na liście trzy możliwości. how to - jest to krótkie ' \
          'wprowadzenie do aplikacji co zawiera i jak ją używać. Następnie jest working, znajduje się tam krótki ' \
          'opis tego co w aplikacji działa. Na końcu listy jest dział info mówiacy o głównych przyczynasz powstania ' \
          'aplikacji jak i autor który ją napisał\n\n               Lewy blok\n' \
          'Znajdują się tu interesujące tematy do opisania. Z początku lista jest pusta, klikając lewy przycisk myszy' \
          'i wybierając "new item" mamy możliwość dodania interesującego nas zagadnienie, jest również możliwość' \
          'usuwania elementów.\n\n               Prawy blok\n Jest to po prostu prostu plik tekstowy, służący do ' \
          'przechowywania interesujących nas treści'
    info = 'Projekt napisany w pyqt5, przygotowany na zaliczenie QT\n\nKrzysztof Jóźwikowski'
    done =   '04.03.2021\nNew w menubar tworzy nową liate, zaczyna cały projekt od nowa\n'\
             'Poprawienie funkcjonowania aplika - new/open/save\n'\
             'Ustawienie readOly na textedit\n'\
             'how to - jest to manual jak używać program\n\n\n'\
             '03.03.2021\nWygląd aplikacji plik View - menubar, lista danych, tekst danych'\
             'manubar i wszystkie w zawrte w nim kategorie - bez fukcjonalności\n'\
             'listWidget w których zawrta są nazwy obiektów do nauki\n'\
             'textedit w którym umieszczamy tekst do nauki interesującego nas zagadnienia\n'\
             'Plik pomocniczy zawierający klase date i lieste w której przechowujemy dane\n'\
             'action New umożliwiająca dodawanie nowego itemu do listy\n'\
             'action save zapisuje dane stoworzone w programie\n'\
             'action open otwiera wchesniej zapisany plik (działa poprawnie dopiero po dadaniu nowego itemu do listy)\n'\
             'help wyswietlający informacje o programie\n'