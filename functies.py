def omzetperperiodevoorproductgroep(productenlijst, productgroep):
    """

    This function checks if each product in the productenlijst is equal to the given superproductgroep. He’ll sum the
    total amount.
    :param productenlijst: dictionary
    :param productgroep: string
    :return: float

    """
    # We always start at 0
    sum = 0.0
    for product in productenlijst:
        # If the productgroep of the product is equal to the given superproductgroep of the function.
        if product['productgroep (keuzelijst)'] == productgroep:
            # add the amoumt to the total supergroep
            sum += float(product["inkoopvolume"].replace(",", "."))
    if sum > 0.0:
        return sum
    # if the number is less than 0.0
    return 0



def omzetperperdiodevoorsuperproductgroep(productenlijst, superproductgroepenlijst):
    """
    This function checks if the superproductgroep is equal to the productgroepen in the superproductgroepenlijst,
    than he wil sums up the same items. It will return a dictionary
    :param productenlijst: string
    :param superproductgroepenlijst: dictionary of lists
    :return: dictionary of lists

    """
    dictionary = {}
    # for each item in the supergroepenlijst, the system checks if the item occurs often.
    for spg, productgroepen in superproductgroepenlijst.items():
        totaal = 0.0
        # for each productgroep in the productgroepen, a dictionary will be made
        for pg in productgroepen:
            totaal += omzetperperiodevoorproductgroep(productenlijst, pg)
        dictionary[spg] = totaal

    return dictionary

