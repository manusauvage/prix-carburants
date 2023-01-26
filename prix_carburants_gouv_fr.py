#! /usr/bin/env python
# coding: utf-8

"""
Parses open gas prices XML data published by the French government
at https://www.prix-carburants.gouv.fr/rubrique/opendata/ and computes:
- the average price (nationwide) for SP95-E10 unleaded gasoline and E85
- the density/price ratio for these two types of gasoline

The goal is to allow comparisons of the density/price ratio for E10/E85
over time.
"""


import sys
import statistics
from tqdm.auto import tqdm
import xml.etree.cElementTree as ET


def mean_price_and_density(gas_name, price_data):
    if gas_name == 'E10':
        density = 10
    elif gas_name == 'E85':
        density = 6.5
    else:
        # So far, we only process E10 and E85 gas types.
        # We have no information about the density of other gas types.
        # FIXME: this should probably be changed to make the script
        # FIXME: more useful/versatile
        raise ValueError(f"Densité inconnue pour ce type d'essence: {gas_name}")
    mean = statistics.mean(price_data)
    ratio = density / mean
    return (mean, ratio)

def parse_gas_prices_xml(xmlfile, gas_filter=('E10', 'E85')):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    # data is a dict with gas types as main keys.
    # for gas type, two arrays are built:
    # - one with the list of gas station selling this type of gas
    # - one with the list of all available prices for that gas type
    data = {}
    for pdv in tqdm(root.findall('pdv')):
        pdv_id = pdv.get('id')
        prices = pdv.findall('prix')
        for price in prices:
            gas_name = price.get('nom')
            if not gas_name in gas_filter:
                continue
            gas_price = float(price.get('valeur'))
            # Price data is not consistent, it can be expressed in euros
            # (e.g. 1.234), or in tenth of cents (e.g. 1234).
            # As of today, any price per liter above 10€ is an anomaly and
            # probably indicates that we're dealing with tenth of cents
            # and not euros.
            if gas_price > 10.:
                gas_price = gas_price / 1000.

            if not gas_name in data:
                data[gas_name] = {}
                data[gas_name]['prices'] = []
                data[gas_name]['stations'] = {}
            data[gas_name]['prices'].append(gas_price)
            if not pdv_id in data[gas_name]['stations']:
                data[gas_name]['stations'][pdv_id] = True
    return data


if __name__ == '__main__':
    url = 'https://www.prix-carburants.gouv.fr/rubrique/opendata/'
    if len(sys.argv) != 2:
        print(
            f'usage : {sys.argv[0]} <fichier XML>'
            f'\nles données officielles sont publiées ici : {url}'
            )
        sys.exit(1)
    sys.stdout.write("Chargement du fichier XML, si le fichier est gros c'est un peu long...\r")
    gas_data = parse_gas_prices_xml(sys.argv[1])
    for gas_type in ['E10', 'E85']:
        mean_price, density_ratio = mean_price_and_density(
            gas_type,
            gas_data[gas_type]['prices']
            )
        nb_stations = len(gas_data[gas_type]['stations'])
        print(
            f'{nb_stations} stations vendent du {gas_type}'
            f' - Prix moyen: {mean_price:.3f}'
            f' - rapport densité/prix: {density_ratio:.3f}'
        )
