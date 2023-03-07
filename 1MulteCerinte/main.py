from Domain.jocSahValidator import JocSahValidator
from Domain.jucatorValidator import JucatorValidator
from Repository.json_repository import JsonRepository
from Service.jocSahService import JocSahService
from Service.jucatorService import JucatorService
from UserInterface.Console import Console

"""
de retinut sa exersez liste
adica sa iau un parametru ca lista in repo
am un ex cu lista in lab sau examen de la iulia 
"""
def main():
    jucatorRepository = JsonRepository("jucator.json")
    jucatorValidator = JucatorValidator()
    jucatorService = JucatorService(jucatorRepository, jucatorValidator)

    jocSahRepository = JsonRepository("jocSah.json")
    jocSahValidator = JocSahValidator()
    jocSahService = JocSahService(jocSahRepository, jocSahValidator,jucatorRepository)

    console = Console(jucatorService, jocSahService)
    console.runConsole()


if __name__ == '__main__':
    main()