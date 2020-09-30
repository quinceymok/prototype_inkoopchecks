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

supergroepenlijst = {
    "Broodbeleg_hartig": ["Broodbeleg hartig (self-service/kleinverpakking)", "Broodbeleg hartig (vers bereide "
                                                                              "broodjes)"],
    "Broodbeleg_zoet": ["Broodbeleg zoet (self-service/kleinverpakking)", "Broodbeleg zoet (vers bereide broodjes)"],
    "Snacks_zoet": ["Snacks (zoet)"],
    "Snacks_Hartig": ["Snacks (hartig)"],
    "Handfruit_(snack)groente": ["Fruit (handfruit/self-service)", "Groente (snack/self-service)"],
    "Dranken": ["Dranken (alcoholisch)", "Dranken (niet alcoholisch)"],
    "Kant_klaar_maaltijden": ["Kant en klaar maaltijden"],
    "Frituur_bladerdeegproducten": ["Frituur en bladerdeegproducten"],
    "Graanproducten": ["Graanproducten (self-service)"],
    "Zuivel_(exclusief zuiveldranken)_kaas_en_eieren": ["Eieren", "Kaas", "Zuivel (exclusief zuiveldranken)"],
    "Graanproducten_aardappelen": ["aardapppelen & knolgewassen", "Graanproducten en bindmiddelen (voor vers bereide "
                                                                  "gerechten)"],
    "Vlees_vis": ["Vis  (exclusief broodbeleg)", "Vlees en gevogelte (exclusief vleeswaren)"],
    "Vleesvervangers": ["Vleesvervangers (exclusief vleeswaren)"],
    "Peulvruchten_noten_zaden": ["Noten en zaden", "Peulvruchten"],
    "Overig (sauzen, vetten, kruiden en suikers)": ["Diversen", "Hartige sauzen", "Kruiden en specerijen", "Suiker en "
                                                                                                           "zoetwaren",
                                                    "Vetten en oliën"],

}

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


def omzetperperiodevoorproductgroep(productenlijst, productgroep):
    # We beginnen altijd bij 0
    sum = 0
    # voor elk product die we in onze bovenstaande productenlijst hebben
    for product in productenlijst:
        # als de productgroep van het product in de productenlijst gelijk is aan de meegegeven superproductgroep vd
        # functie
        if product["productgroep (keuzelijst)"] == productgroep:
            # voeg het bedrag bij het totaal toe
            sum += product["inkoopvolume € (invullen)"]
    # return zodat de functie iets teruggeeft
    return sum


def omzetperperdiodevoorsuperproductgroep(productenlijst, supergroepenlijst):
    for spg, productgroepen in supergroepenlijst.items():
        totaal = 0
        for pg in productgroepen:
            totaal += omzetperperiodevoorproductgroep(productenlijst, pg)
        print(spg + ": " + str(totaal))


omzetperperdiodevoorsuperproductgroep(productenlijst, supergroepenlijst)
# print(omzetperperiodevoorproductgroep(productenlijst, "Graanproducten en bindmiddelen (voor vers bereide gerechten)"))
