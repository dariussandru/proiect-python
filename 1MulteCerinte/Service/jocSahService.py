import jsonpickle

from Domain.jocSah import JocSah
from Domain.jocSahValidator import JocSahValidator
from Repository.repository import Repository


class JocSahService:
    def __init__(self, jocRepository: Repository,
                 jocValidator: JocSahValidator,
                 jucatoriRepository: Repository):

        self.jocRepository = jocRepository
        self.jocValidator = jocValidator
        self.jucatoriRepository = jucatoriRepository

    def adaugare(self, idJoc: str, jucatorAlb: int, jucatorNegru: int, rezultat: str, dataInregistrariiJocului):

        joc = JocSah(idJoc, jucatorAlb, jucatorNegru, rezultat, dataInregistrariiJocului)
        if self.jucatoriRepository.read(jucatorAlb) is None:
            raise KeyError(f"Nu exista jucatorul alb cu id-ul dat {jucatorAlb}")
        if self.jucatoriRepository.read(jucatorNegru) is None:
            raise KeyError(f"Nu exista jucatorul negru cu id-ul dat {jucatorNegru}")
        self.jocValidator.valideaza(joc)
        self.jocRepository.create(joc)

    def stergere(self, idJoc: str):
        self.jocRepository.stergere(idJoc)

    def modificare(self, idJoc: str, jucatorAlb: int, jucatorNegru: int, rezultat: str, dataInregistrariiJocului):
        joc = JocSah(idJoc, jucatorAlb, jucatorNegru, rezultat, dataInregistrariiJocului)
        self.jocValidator.valideaza(joc)
        self.jocRepository.modificare(joc)

    def getAll(self):
        return self.jocRepository.read()

    def stergereJocCascada(self, idJucator: int):
        for joc in self.jocRepository.read():
            if joc.idJucatorAlb or joc.idJucatorNegru == idJucator:
                self.jocRepository.stergere(joc.id_entity)

    def afisareJocIntreDouaZile(self, zi1, zi2):
        rezultat = []
        for x in self.jocRepository.read():
            if zi1 < int(x.dataInregistrariiJocului.day) < zi2:
                rezultat.append(x)
        print(rezultat)

    def stergereJocDintroZi(self, dataCitita):
        for x in self.jocRepository.read():
            if int(x.dataInregistrariiJocului.day) == dataCitita:
                self.jocRepository.stergere(x.id_entity)

    def jucatoriOrdonatiDupaNrVictorii(self):
        idJucatoriNrVictorii = {}
        for jucatori in self.jucatoriRepository.read():
            idJucatoriNrVictorii[jucatori.id_entity] = 0
        for joc in self.jocRepository.read():
            if joc.idJucatorAlb:
                idJucatoriNrVictorii[joc.idJucatorAlb] += 1
            elif joc.idJucatorNegru:
                idJucatoriNrVictorii[joc.idJucatorNegru] += 1

        rezultat = []
        for idJucatori in idJucatoriNrVictorii:
            rezultat.append({"jucatorul": self.jucatoriRepository.read(idJucatori),
                             "nrVictorii": idJucatoriNrVictorii[idJucatori]})
        print(sorted(rezultat, key=lambda x:x["nrVictorii"], reverse=True))

    def exportJson(self, filename: str):

        test = []
        rezultat = {}
        for jucator in self.jucatoriRepository.read():
            rezultat[jucator.nume] = []

        for joc in self.jocRepository.read():
            jucatorAlb = self.jucatoriRepository.read(joc.idJucatorAlb)
            jucatorNegru = self.jucatoriRepository.read(joc.idJucatorNegru)
            rezultat[jucatorAlb.nume].append(jucatorNegru.nume)

        with open(filename, "w") as f:
            f.write(jsonpickle.dumps(rezultat))
