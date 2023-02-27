from math import*
from random import*
from module1 import*

#16 number
palgad = [1200, 2500, 750, 395, 1200]
inimesed = ["A", "B", "C", "D", "E"]

uuendatud_inimesed = []
for i in range(len(inimesed)):
    if (i+1) % 3 == 0:
        uued_nimed = input(f"Sisestage uus nimi {inimesed[i]}: ")
        uuendatud_inimesed.append(uuendatud_inimesed)

uuendatud_inimesed ,uuendatud_inimesed = nimeta_iga_kolmanda_inimene_ümber(inimesed, uued_nimed)
print(uuendatud_inimesed)

#6 number

palgad = [1200,2500,750,395,1200]
inimesed = ["A","B","C","D","E"]

leia_samad_palgad(palgad, inimesed)

