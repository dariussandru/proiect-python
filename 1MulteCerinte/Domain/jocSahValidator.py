from Domain.jocSah import JocSah


class JocSahValidator:
    def valideaza(self, jocSah: JocSah):
        erori = []
        rezultat = ["victorie", "egal", "infrangere"]
        if int(jocSah.idJucatorAlb) <= 0:
            erori.append("Nu exista jucatorul alb cu id-ul dat")
        if int(jocSah.idJucatorNegru) <= 0:
            erori.append("Nu exista jucatorul negru cu id-ul dat")
        if jocSah.rezultat not in rezultat:
            erori.append("Nu exista acest rezultat")
        if jocSah.dataInregistrariiJocului is None:
            erori.append("Data inregistrarii jocului trebuie sa fie de forma'dd.mm.yyyy'")
        if len(erori) > 0:
            raise KeyError(erori)