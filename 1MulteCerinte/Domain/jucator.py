from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Jucator(Entity):
    nume: str
    nrVictorii: int
    nrRemize: int
    nrInfrangeri: int
    oCalitate: str
