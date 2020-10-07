import csv
import functies

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


with open('csv/Dataexcelcsv.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    data = list(reader)

functies.omzetperperdiodevoorsuperproductgroep(data, supergroepenlijst)
