# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class Użytkownik:
    def __init__(self, imię, wiek, waga, wzrost, płeć, aktywność):
        self.imię = imię
        self.wiek = wiek
        self.waga = waga
        self.wzrost = wzrost
        self.płeć = płeć
        self.aktywność = aktywność

    def oblicz_bmr(self):
        if self.płeć.lower() == 'mężczyzna':
            BMR = 10 * self.waga + 6.25 * self.wzrost - 5 * self.wiek + 5
        elif self.płeć.lower() == 'kobieta':
            BMR = 10 * self.waga + 6.25 * self.wzrost - 5 * self.wiek - 161
        else:
            raise ValueError("Nieprawidłowa wartość płci. Użyj 'mężczyzna' lub 'kobieta'.")
        return BMR

    def oblicz_dzienne_kalorie(self):
        BMR = self.oblicz_bmr()

        # poziom aktywności fizycznej
        if self.aktywność.lower() == 'niska':
            kalorie = BMR * 1.2
        elif self.aktywność.lower() == 'średnia':
            kalorie = BMR * 1.55
        elif self.aktywność.lower() == 'wysoka':
            kalorie = BMR * 1.9
        else:
            raise ValueError("Nieprawidłowy poziom aktywności. Użyj 'niska', 'średnia' lub 'wysoka'.")
        return kalorie

def dodaj_użytkownika():
    imię = input("Podaj imię użytkownika: ")
    wiek = int(input("Podaj wiek: "))
    waga = float(input("Podaj wagę (w kg): "))
    wzrost = int(input("Podaj wzrost (w cm): "))
    płeć = input("Podaj płeć (mężczyzna/kobieta): ")
    aktywność = input("Podaj poziom aktywności (niska/średnia/wysoka): ")

    użytkownik = Użytkownik(imię, wiek, waga, wzrost, płeć, aktywność)
    return użytkownik

użytkownicy = []

#  kilka użytkowników
for _ in range(2):
    użytkownik = dodaj_użytkownika()
    użytkownicy.append(użytkownik)

#  dzienne zapotrzebowanie kaloryczne dla każdego użytkownika, wyświetlane wyniki oddzielnie
for użytkownik in użytkownicy:
    kalorie = użytkownik.oblicz_dzienne_kalorie()
    print(f"Dzienne zapotrzebowanie kaloryczne dla {użytkownik.imię}: {kalorie} kcal")


#checklist

pip install pandas openpyxl
import pandas as pd

def wczytaj_dane_excel(produkty.xlsx):
    df = pd.read_excel(produkty.xlsx)
    return df

def utworz_checklist(df):
    checklist = df[['Produkt', 'Zaznaczone']].copy()
    checklist['Zaznaczone'] = False
    return checklist

def zaznacz_produkt(checklist, produkt):
    checklist.loc[checklist['Produkt'] == produkt, 'Zaznaczone'] = True

def zapisz_do_excel(checklist, checklist.xlsx):
    checklist.to_excel(checklist.xlsx, index=False)

if __name__ == "__main__":
    nazwa_pliku_excel = 'twoj_plik.xlsx'

    dane = wczytaj_dane_excel(produkty.xlsx)
    checklist = utworz_checklist(dane)

    while True:
        print("\nAktualna checklista:")
        print(checklist)

        produkt_do_zaznaczenia = input("\nPodaj nazwę produktu do zaznaczenia (lub 'exit' aby zakończyć): ")

        if produkt_do_zaznaczenia.lower() == 'exit':
            break

        if produkt_do_zaznaczenia in checklist['Produkt'].values:
            zaznacz_produkt(checklist, produkt_do_zaznaczenia)
            print(f"Produkt '{produkt_do_zaznaczenia}' zaznaczony.")
        else:
            print(f"Produkt '{produkt_do_zaznaczenia}' nie znaleziony.")

    nazwa_nowego_pliku_excel = 'checklist_po_zaznaczeniu.xlsx'
    zapisz_do_excel(checklist, nazwa_nowego_pliku_excel)

    print(f"\nChecklista po zaznaczeniu zapisana do pliku: {nazwa_nowego_pliku_excel}")
