import functies, unittest, csv


class Testformulasmethods(unittest.TestCase):

    def testminus(self):
        """Deze functie test of het goed gaat als de som eindigt op minus"""
        with open('csv/test_inkoopcheck_1.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)
        a = functies.omzetperperiodevoorproductgroep(data, "Graanproducten")
        b = 0
        self.assertEqual(a, b)

    def test_2(self):
        """Deze test checkt of de productgroepen die niet in de productenlijst staan worden meegerekend"""
        with open('csv/test_inkoopcheck_2.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)
        a = functies.omzetperperiodevoorproductgroep(data, "Havermoutproducten")
        b = 0
        self.assertEqual(a, b)

    def test_3(self):
        """deze test checks of de som nog steeds bij elkaar wordt opgeteld, wanneer de waardes van de inkoopvolumes in
        kommagetallen worden vermeld """
        with open('csv/test_inkoopcheck_3.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)
        a = functies.omzetperperiodevoorproductgroep(data, "Graanproducten en bindmiddelen (voor vers bereide "
                                                           "gerechten)")
        b = 106.9
        self.assertEqual(a, b)

    def test_4(self):
        """ Deze test checkt of de dictionaries gelijk zijn aan elkaar"""

        supergroepenlijst = {
            'Graanproducten_aardappelen': ['Graanproducten en bindmiddelen (voor vers bereide gerechten)',
                                           'aardapppelen & knolgewassen'],
            'Broodbeleg hartig': ['Broodbeleg hartig (self-service/kleinverpakking)',
                                  'Broodbeleg hartig (vers bereide broodjes)'],
            "Broodbeleg_zoet": ['Broodbeleg zoet (self-service/kleinverpakking)',
                                'Broodbeleg zoet (vers bereide broodjes)'],
            "Snacks_zoet": ["Snacks (zoet)"],
            "Snacks_Hartig": ["Snacks (hartig)"],
            "Handfruit_(snack)groente": ["Fruit (handfruit/self-service)", "Groente (snack/self-service)"],
            "Dranken": ["Dranken (alcoholisch)", "Dranken (niet alcoholisch)"],
            "Kant_klaar_maaltijden": ["Kant en klaar maaltijden"],
            "Frituur_bladerdeegproducten": ["Frituur en bladerdeegproducten"],
            "Graanproducten": ["Graanproducten (self-service)"],
            "Zuivel_(exclusief zuiveldranken)_kaas_en_eieren": ["Eieren", "Kaas", "Zuivel (exclusief zuiveldranken)"], }

        with open('csv/test_inkoopcheck_4.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            data = list(reader)
        a = functies.omzetperperdiodevoorsuperproductgroep(data, supergroepenlijst)
        b = {'Broodbeleg hartig': 223.8,
             'Broodbeleg_zoet': 0.0,
             'Dranken': 112.5,
             'Frituur_bladerdeegproducten': 0.0,
             'Graanproducten': 0.0,
             'Graanproducten_aardappelen': 365.0,
             'Handfruit_(snack)groente': 0.0,
             'Kant_klaar_maaltijden': 0.0,
             'Snacks_Hartig': 0.0,
             'Snacks_zoet': 277.9,
             'Zuivel_(exclusief zuiveldranken)_kaas_en_eieren': 0.0}
        self.assertEqual(a, b)
