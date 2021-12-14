def openbestand():
    '''opent het bestand
    input: het excel bestand
    '''
    open_bestand = open(bestand, 'r')
    read = open_bestand.readline().split().strip()
    for i in open_bestand:
        regel = i.split('\t')
        # variation reads =< 5
        # SNP state is leeg (blank)
        # Synonomous = 'FALSE'
        # if 'Retinitis' in OMIM_DISEASE
        # Gene component = SA_SITE, EXON_REGION

        if 'Retinitis' in regel[]:



def soorteren():
    '''filtrert het excel bestand
    input: excel bestand
    output: gefiltreerde gegevens
    '''

def main():
    bestand = '21213_exome_hcdiffs.txt'
    openbestand()
    soorteren()

main()