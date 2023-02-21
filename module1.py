def leia_samad_palgad(palgad, inimesed):
    palgad_counts = []      #count/числа
    for i in range(len(palgad)):       #присваивает переменной значение/ повторяя код(используя Len-(Возвращает количество символов или же зарплату))
        if palgad[i] in palgad_counts:        
            palgad_counts[palgad[i]].append(inimesed[i])
        else:
            palgad_counts[i] = [inimesed[i]]
    for palgad in palgad_counts:
        if len(palgad_counts[palgad]) > 1:
            print(f"Järgmistel {len(palgad_counts[palgad])} inimestel on palk {palgad}: {','.join(palgad_counts[palgad])}")


           