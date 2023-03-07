from Domain.jucator import Jucator


class JucatorValidator:
    def valideaza(self, jucator: Jucator):
        erori = []
        if int(jucator.id_1entity) <= 0:
            erori.append("Id-ul trebuie sa fie pozitiv")
        if int(jucator.nrVictorii) < 0:
            erori.append("Eroare de scriere, victoriile nu pot fi negative")
        if int(jucator.nrRemize) < 0:
            erori.append("Eroare de scriere, remizele nu pot fi negative")
        if int(jucator.nrInfrangeri) < 0:
            erori.append("Eroare de scriere, infrangerile nu pot fi negative")
        if jucator.oCalitate is None:
            erori.append("Trebuie specificat ceva la descriere")
        if len(erori) > 0:
            raise ValueError(erori)