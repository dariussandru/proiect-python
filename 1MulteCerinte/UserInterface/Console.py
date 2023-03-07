from datetime import datetime

from Service.jocSahService import JocSahService
from Service.jucatorService import JucatorService


def readDate(dataString):
    try:
        return datetime.strptime(dataString, "%d.%m.%Y").date()
    except ValueError:
        return None


def afiseaza(entitati):
    for entitate in entitati:
        print(entitate)


class Console:
    def __init__(self, jucatorService: JucatorService, jocSahService: JocSahService):

        self.jucatorService = jucatorService
        self.jocSahService = jocSahService

    def runConsole(self):
        while True:
            print()
            print("1. Adauga jucator ")
            print("2. Stergere jucator ")
            print("3. Modifica jucator")
            print("____________________")
            print("4. Adauga joc de sah")
            print("5. Stergere joc de sah")
            print("6. Modificare joc de sah")
            print("____________________")
            print("f1. Ordonarea jucatorilor in juncatie de un criteriu dat")
            print("f2. Sterge un jucator in cascada")
            print("f3. Afiseaza nr de victorii+remize pentru un jucator")
            print("f4. Afiseaza meciurile dintr-un interval de zile")
            print("f5. Afisare toti jucatorii care au in descriere un cuvant dat")  # cautare full text
            print("f6. Stergere joc dintr-o zi data de la tastatura")
            print("f7. Jucator  i ordonati dupa nr de meciuri jucate")
            print("f8. Export Json")
            print("____________________")
            print("a1. Afiseaza toti jucatori")
            print("a2. Afiseaza toate jocuri")
            print("x. Iesire ")
            print("")
            optiune = input("Dati o optiune ")

            if optiune == "1":
                self.adaugaJucator()
                afiseaza(self.jucatorService.getAll())
                print("Jucatorul a fost adaugat cu succes!")
                """stergere in cascada"""
            elif optiune == "2":
                idJucator = input("Dati id-ul jucatorului pe care doriti sa-l stergeti ")
                self.stergeJucator(idJucator)
                print("Jucatorul a fost sters cu succes!")
            elif optiune == "3":
                self.modificaJucator()
                print("Jucatorul a fost modificat cu succes!")
                """--------------------------------------------------------------------"""
            elif optiune == "4":
                self.adaugaJoc()
                print("Jocul a fost adaugat cu succes!")
            elif optiune == "5":
                idJoc = input("Dati id-ul jocului pe care diriti sa-l stergeti")
                self.stergeJoc(idJoc)
                print("Jocul a fost sters cu succes!")
            elif optiune == "6":
                self.modificareJoc()
                print("Jucatorul a fost modificat cu succes!")
                """--------------------------------------------------------------------"""
            elif optiune == "f1":
                afiseaza(self.jucatorService.ordonareCrescatorDupaUnCriteriu())
            elif optiune == "f2":
                idJucator = input("Dati id-ul jucatorului pe care doriti sa-l stergeti in cascada")
                self.stergeJucator(idJucator)
                self.jocSahService.stergereJocCascada(idJucator)
                print("Stergerea in cascada a fost fost efectuata cu succes!")
            elif optiune == "f3":
                idJucator = input("Dati id-ul jucatorului caruia vreti sa aflati nrvitorii+nrRemize")
                self.jucatorService.afisareCastiguriPlusRemize(idJucator)
            elif optiune == "f4":
                zi1 = int(input("Dati prima zi "))
                zi2 = int(input("Dati a doua zi "))
                self.jocSahService.afisareJocIntreDouaZile(zi1, zi2)
            elif optiune == "f5":
                cuvant = input("Dati un cuvant pe care vreti sa-l cautati in Jucatori ")
                self.jucatorService.cautareFullText(cuvant)
            elif optiune == "f6":
                data = int(input("Dati ziua din care vreti sa stergeti meciurile "))
                self.jocSahService.stergereJocDintroZi(data)
                print("Stergerea jocului efectuata cu succes!")
            elif optiune == "f7":
                self.jocSahService.jucatoriOrdonatiDupaNrVictorii()
            elif optiune == "f8":
                filename = input("Dati numele fisierului ")
                self.jocSahService.exportJson(filename)
                """--------------------------------------------------------------------"""
            elif optiune == "a1":
                afiseaza(self.jucatorService.getAll())
            elif optiune == "a2":
                afiseaza(self.jocSahService.getAll())

            elif optiune == "x":
                break

    def adaugaJucator(self):
        try:
            idJucator = input("Dati id-ul jucatorului ")
            nume = input("Dati numele jucatorului ")
            nrVictorii = input("Dati nr de victorii ")
            nrRemize = input("Dati nr de remize ")
            nrInfrangeri = input("Dati nr de infrangeri ")
            oCalitate = input("Dati o calitate a jucatorului ")

            self.jucatorService.adaugare(idJucator, nume, nrVictorii, nrRemize, nrInfrangeri, oCalitate)
        except Exception as ex:
            print("Eroare:", ex)

    def stergeJucator(self, idJucator: str):
        try:
            self.jucatorService.stergere(idJucator)
        except Exception as ex:
            print("Eroare:", ex)

    def modificaJucator(self):
        try:
            idJucator = input("Dati id-ul jucatorului pe care doriti sa-l modificati ")
            nume = input("Dati noul nume al jucatorului ")
            nrVictorii = input("Dati noul numar de victorii ")
            nrRemize = input("Dati noul numar de remize ")
            nrInfrangeri = input("Dati noul numar de infrangeri ")
            descriere = input("Dati noua descriere a jucatorului")

            self.jucatorService.modificare(idJucator, nume, nrVictorii, nrRemize, nrInfrangeri, descriere)
        except Exception as ex:
            print("Eroare:", ex)

    def adaugaJoc(self):
        try:
            idJoc = input("Dati id-ul jocului ")
            idJucatorAlb = input("Dati id-ul jucatorului alb ")
            idJucatorNegru = input("Dati id-ul jucatorului negru ")
            rezultat = input("Dati un rezultat, rezultatul poate fi : victorie, egal, infrangere ")
            data = input("Dati data inregistrarii jocului")
            dataInregistrariiJocului = readDate(data)

            self.jocSahService.adaugare(idJoc, idJucatorAlb, idJucatorNegru, rezultat, dataInregistrariiJocului)
        except Exception as ex:
            print("Eroare:", ex)

    def stergeJoc(self, idJoc: str):
        try:
            self.jocSahService.stergere(idJoc)
        except Exception as ex:
            print("Eroare:", ex)

    def modificareJoc(self):
        try:
            idjoc = input("Dati id-ul jocului pe care doriti sa-l modificati")
            idJucatorAlb = input("Dati id-ul jucatorului alb")
            idJucatorNegru = input("Dati id-ul jucatorului negru")
            rezultat = input("Dati noul rezultat , rezultatele pot fi : victorie, egal , infrangere")
            data = input("Dati noua daca a intregistrarii jocului")
            dataInregistrariiJocului = readDate(data)

            self.jocSahService.modificare(idjoc, idJucatorAlb, idJucatorNegru, rezultat, dataInregistrariiJocului)
        except Exception as ex:
            print("Eroare:", ex)
