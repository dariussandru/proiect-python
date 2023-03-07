from dataclasses import dataclass
from datetime import date

from Domain.entity import Entity

@dataclass
class JocSah(Entity):
    idJucatorAlb: int
    idJucatorNegru: int
    rezultat: str
    dataInregistrariiJocului: date
