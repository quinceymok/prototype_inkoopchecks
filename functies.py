def omzetperperiodevoorproductgroep(productenlijst, productgroep):
    # We beginnen altijd bij 0
    sum = 0.0
    # voor elk product die we in onze bovenstaande productenlijst hebben
    for product in productenlijst:
        # als de productgroep van het product in de productenlijst gelijk is aan de meegegeven superproductgroep vd
        # functie
        if product['productgroep (keuzelijst)'] == productgroep:
            # voeg het bedrag bij het totaal toe
            sum += float(product["inkoopvolume"].replace(",", "."))
    if sum > 0.0:
        return sum
    return 0


def omzetperperdiodevoorsuperproductgroep(productenlijst, supergroepenlijst):
    # voor elk item in de supergroeplijst checkt het systeem of een item vaker voorkomt
    dictionary = {}
    for spg, productgroepen in supergroepenlijst.items():
        totaal = 0.0
        # voor elke productgroep in de productgroepen maakt hij er een dictionary van
        for pg in productgroepen:
            totaal += omzetperperiodevoorproductgroep(productenlijst, pg)
        dictionary[spg] = totaal

    return dictionary

