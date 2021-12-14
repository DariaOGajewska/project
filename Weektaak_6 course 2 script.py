def openbestand(bestand):
    '''opent het bestand
    input: het excel bestand
    '''
    open_bestand = open(bestand, 'r')
    read = open_bestand.readline()
    for i in open_bestand:
        #for i in range(0, 5):
        regel = i.strip().split('\t')
    print(i)
    print(regel)
            # variation reads =< 5
            # SNP state is leeg (blank)
            # Synonomous = 'FALSE'
            # if 'Retinitis' in OMIM_DISEASE
            # Gene component = SA_SITE, EXON_REGION


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