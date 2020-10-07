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
