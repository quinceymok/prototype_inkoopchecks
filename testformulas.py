# begin van alle supergroepen
broodbeleg_hartig = {
    "productgroepen": ["selfservice/kleineverpakking", "verse broodjes"],
    "formule": 1
}
broodbeleg_zoet = {
    "productgroepen": ["selfservice/kleineverpakking", "verse broodjes"],
    "formule": 1
}
graanproducten_aardappelen = {
    "productgroepen": ["aardapppelen & knolgewassen", "Graanproducten en bindmiddelen (voor vers bereide gerechten)"],
    "formule": 2
}
# einde van alle supergroepen

productenlijst = [
    {
        "Omschrijving product": "(BAKZ)HANDG. DESEM VOLK. GESN.",
        "soort product (keuzelijst)": "Vegetarisch (weinig zuivel/kaas)",
        "productgroep (keuzelijst)": "Graanproducten en bindmiddelen (voor vers bereide gerechten)",
        "inkoopvolume € (invullen)": 20.20
    },
    {
        "omschrijving product": "(CP 1)VGB.TURKS BROOD",
        "soort product (keuzelijst)": "Vegetarisch (weinig zuivel/kaas)",
        "productgroep (keuzelijst)": "Graanproducten en bindmiddelen (voor vers bereide gerechten)",
        "inkoopvolume € (invullen)": 8
    }
]

def omzetperperiodevoorproductgroep(productenlijst, superproductgroep):
    # We beginnen altijd bij 0
    sum = 0
    # voor elk product die we in onze bovenstaande productenlijst hebben
    for product in productenlijst:
        # als de productgroep van het product in de productenlijst gelijk is aan de meegegeven superproductgroep vd functie
        for productgroep in superproductgroep:
            if productgroep["productgroepen"] == superproductgroep:
                if product["productgroep (keuzelijst)"] == superproductgroep:
                    #voeg het bedrag bij het totaal toe
                    sum += product["inkoopvolume € (invullen)"]
    #return zodat de functie iets teruggeeft
    return sum


print(omzetperperiodevoorproductgroep(productenlijst, graanproducten_aardappelen))