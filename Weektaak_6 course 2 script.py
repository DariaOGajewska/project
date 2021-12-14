def filter(bestand):
    '''Opent het bestand en filtert genen op basis van geselecteerde kenmerken
    input: het excel bestand
    output: genen lijst
    '''

    lijst = []
    open_bestand = open(bestand, 'r')
            # De eerste regel overslaan m.b.v readline()
    header = open_bestand.readline()

    for i in open_bestand:
            # Split regels op tabs, voegt in een lijst
        regel = i.strip().split('\t')

            # Aan welke eigenschappen een gen moet voldoen:
            # 'variation reads' =< 5
            # 'SNP state' = leeg (blank)
            # 'Synonomous' = 'FALSE'
            # 'Gene component' = SA_SITE, EXON_REGION
            # 'Retinitis' in 'OMIM_DISEASE' kolom

            # Het aantal kolommen > 61 (bij sommige regels ontbreken gegevens)
        if len(regel) > 61:
            if int(regel[6]) >= 5:
                if regel[13] == '':
                    if regel[44] == 'FALSE':
                        if regel[33] == 'SA_SITE' or regel[33] == 'EXON_REGION':
                            if 'Retinitis' in regel[61]:
                                lijst.append(regel[24])
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
            else:
                continue
        else:
            continue

    open_bestand.close()
    print('Found genes:', lijst)


def main():
    bestand = '21213_exome_hcdiffs.txt'
    filter(bestand)

main()