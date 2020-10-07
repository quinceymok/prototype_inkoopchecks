import csv

supergroepenlijst = {
    'Graanproducten_aardappelen': ['Graanproducten en bindmiddelen (voor vers bereide gerechten)', 'aardapppelen & knolgewassen'],
    'Broodbeleg hartig': ['Broodbeleg hartig (self-service/kleinverpakking)', 'Broodbeleg hartig (vers bereide broodjes)'],
    "Broodbeleg_zoet": ['Broodbeleg zoet (self-service/kleinverpakking)', 'Broodbeleg zoet (vers bereide broodjes)'],
    "Snacks_zoet": ["Snacks (zoet)"],
    "Snacks_Hartig": ["Snacks (hartig)"],
    "Handfruit_(snack)groente": ["Fruit (handfruit/self-service)", "Groente (snack/self-service)"],
    "Dranken": ["Dranken (alcoholisch)", "Dranken (niet alcoholisch)"],
    "Kant_klaar_maaltijden": ["Kant en klaar maaltijden"],
    "Frituur_bladerdeegproducten": ["Frituur en bladerdeegproducten"],
    "Graanproducten": ["Graanproducten (self-service)"],
    "Zuivel_(exclusief zuiveldranken)_kaas_en_eieren": ["Eieren", "Kaas", "Zuivel (exclusief zuiveldranken)"],

}


def omzetperperiodevoorproductgroep(productenlijst, productgroep):
    # We beginnen altijd bij 0
    sum = 0.0
    # voor elk product die we in onze bovenstaande productenlijst hebben
    for product in productenlijst:
        # als de productgroep van het product in de productenlijst gelijk is aan de meegegeven superproductgroep vd
        # functie
        if product['productgroep (keuzelijst)'] == productgroep:
            # voeg het bedrag bij het totaal toe
            sum += float(product["inkoopvolume"])
    # return zodat de functie iets teruggeeft
    return sum


def omzetperperdiodevoorsuperproductgroep(productenlijst, supergroepenlijsts):
    for spg, productgroepen in supergroepenlijsts.items():
        totaal = 0.0
        for pg in productgroepen:
            totaal += omzetperperiodevoorproductgroep(productenlijst, pg)
        print(spg + ": " + str(totaal))


with open('csv/Dataexcelcsv.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    data = list(reader)

omzetperperdiodevoorsuperproductgroep(data, supergroepenlijst)