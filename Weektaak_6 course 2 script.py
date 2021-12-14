def openbestand():
    '''opent het bestand
    input: het excel bestand
    '''
    open_bestand = open(bestand)
    read = open_bestand.readline().split().strip()
    #for i in open_bestand:


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