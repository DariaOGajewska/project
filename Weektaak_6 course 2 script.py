def openbestand(bestand):
    '''opent het bestand
    input: het excel bestand
    '''

    lijst = []
    open_bestand = open(bestand, 'r')
    header = open_bestand.readline()
    for i in open_bestand:
        regel = i.strip().split('\t')
        if int(regel[6]) >= 5:
            if regel[13] == '':
                if regel[44] == 'FALSE':
                    if 'Retinitis' in regel:
                        if regel[33] == 'SA_SITE' or regel[33] == 'EXON_REGION':
                            lijst.append(regel)
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


def soorteren():
    '''filtrert het excel bestand
    input: excel bestand
    output: gefiltreerde gegevens
    '''

def main():
    bestand = '21213_exome_hcdiffs.txt'
    openbestand(bestand)
    soorteren()

main()