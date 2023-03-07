from Domain.jucator import Jucator
from Domain.jucatorValidator import JucatorValidator
from Repository.repository import Repository


class JucatorService:
    def __init__(self, jucatorRepository: Repository,
                 jucatorValidator: JucatorValidator):

        self.jucatorRepository = jucatorRepository
        self.jucatorValidator = jucatorValidator

    def adaugare(self, idJucator: str, nume: str, nrVictorii: int, nrRemize: int, nrInfrangeri: int, oCalitate: str):

        jucator = Jucator(idJucator, nume, nrVictorii, nrRemize, nrInfrangeri, oCalitate)
        self.jucatorValidator.valideaza(jucator)
        self.jucatorRepository.create(jucator)

    def stergere(self, idJucator: str):

        self.jucatorRepository.stergere(idJucator)

    def modificare(self, idJucator: str, nume: str, nrVictorii: int, nrRemize: int, nrInfrangeri: int, oCalitate: str):

        jucator = Jucator(idJucator, nume, nrVictorii, nrRemize, nrInfrangeri, oCalitate)
        self.jucatorValidator.valideaza(jucator)
        self.jucatorRepository.update(jucator)

    def getAll(self):
        return self.jucatorRepository.read()

    def ordonareCrescatorDupaUnCriteriu(self):
        """
        ordoneaza crescator lista formata din jucatorii
        care au victorii+remize > infrangeri
        :return:
        """
        listaRezultate = []
        for jucator in self.jucatorRepository.read():
            if jucator.nrVictorii + jucator.nrRemize > jucator.nrInfrangeri:
                listaRezultate.append(jucator)

        return sorted(listaRezultate, key=lambda x: x.nrVictorii, reverse=False)  # false-crescator si true-descrescator

    def afisareCastiguriPlusRemize(self, idJucator: str):
        """
        pentru un id dat de la tastatura afiseaza victoriile + remizele
        jucatorului cu id-ul dat
        :return:
        """
        for x in self.jucatorRepository.read():
            if x.id_entity == idJucator:
                suma = int(x.nrVictorii) + int(x.nrRemize)
                print(f"Numarul de victorii + remize este:{suma}")

    def cautareFullText(self, cuvant: str):
        """
        functia toti jucatorii care au la descriere un cuvant dat de la tastatura
        :return: o lista
        """
        rezultat = []
        for x in self.jucatorRepository.read():
            if cuvant in str(x.id_entity) \
                    or cuvant in str(x.nrVictorii)\
                    or cuvant in str(x.nrRemize) \
                    or cuvant in str(x.nrInfrangeri) \
                    or cuvant in str(x.oCalitate):
                rezultat.append(x)
        print(rezultat)