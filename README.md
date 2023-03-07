# proiect-python
Joc de sah.

Functionalitati:
1. CRUD jucator: id, nume, nr victorii, nr remize, nr infrangeri,  o calitate.
2. CRUD joc : id-ul jocului/meciului, id-ul jucatorului cu partea alba, id-ul jucatorului cu partea neagra, rezultat , data.
3. Ordonarea jucatorilor in functie de nr de victorii ( victorii+remize >  infrangeri).
4. Stergerea in cascada a unui jucator ( daca stergi un jucator se sterge si meciul in care el a jucat).
5. Afisarea nr de vitorii+remize pentru un jucator dat de la tastatura.
6. Afisarea meciurilor dintr-un interval de zile dat de la tastatura.
7. Cautare full text si afisare dupa un cuvant dat.
8. Stergerea unui joc dintr-o zi data de la tastatura.
9. Afisare toti jucatori.
10. Afisare toate jocurile.



In rezolvarea problemei de mai sus, se vor este esential sa se tine cont de:
1. Teste și specificații la toate iterațiile.
2. Toate CRUD-urile, minim încă o funcționalitate diferită de CRUD. Cu validări, arhitectură stratificată cu toate elementele descrise la curs. 
3. Salvarea datelor în fișiere json.
4. Repository generic, clase proprii de excepții.
5. Folosirea type hinting, ABC, protocol.
6. Refactorizat toate funcționalitățile posibile folosind map, filter, list comprehensions, reduce, filter.
