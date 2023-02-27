#6
def leia_samad_palgad(palgad, inimesed):
    palgad_counts = {}  
    for i in range(len(palgad)):
        if palgad[i] in palgad_counts:
            palgad_counts[palgad[i]].append(inimesed[i])
        else:
            palgad_counts[palgad[i]] = [inimesed[i]]
    for palganumber, inimesed in palgad_counts.items():
        if len(inimesed) > 1:
           print(f"Järgmistel {len(palgad_counts[palgad])} inimestel on palk {palgad}: {','.join(palgad_counts[palgad])}")



#16
def nimeta_iga_kolmanda_inimene_ümber(inimesed, uued_nimed):
    uuendatud_inimesed = []
    for i, nimi in (inimesed):
        if (i+1) % 3 == 0:  #  3
            if uued_nimed:  # если остались новые имена
                uuendatud_inimesed.append(uued_nimed.pop(0))
            else:
                uuendatud_inimesed.append(nimi)  # использовать новое имя
        else:
            uuendatud_inimesed.append(nimi)
    return uuendatud_inimesed