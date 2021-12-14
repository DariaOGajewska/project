def soorteren(bestand):
    '''opent het bestand, filtreert het bestand
    input: het excel bestand
    output: gefiltreerde gegevens
    '''

    lijst = []
    open_bestand = open(bestand, 'r')
    header = open_bestand.readline()

    for i in open_bestand:
        regel = i.strip().split('\t')

        if len(regel) > 61:
            if int(regel[6]) >= 5:
                if regel[13] == '':
                    if regel[44] == 'FALSE':
                        if regel[33] == 'SA_SITE' or regel[33] == 'EXON_REGION':
                            if 'Retinitis' in regel:
                                lijst.append(regel)
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
            # variation reads =< 5
            # SNP state is leeg (blank)
            # Synonomous = 'FALSE'
            # if 'Retinitis' in OMIM_DISEASE
            # Gene component = SA_SITE, EXON_REGION

    open_bestand.close()
    print(lijst)


def main():
    bestand = '21213_exome_hcdiffs.txt'
    soorteren(bestand)

main()