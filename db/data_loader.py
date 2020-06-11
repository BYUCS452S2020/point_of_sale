import argparse
# from db import postgres
# from view import developer
from db import mongo
import pandas as pd
import sys


def fill_promos(promos_file):
    mongo.delete_all_promos()
    promos = pd.read_csv(promos_file, engine='python')
    for tpl in promos.itertuples():
        #mongo.insert_promo(name, discount)
        mongo.insert_promo(tpl[1], tpl[2])


def fill_taxes(taxes_file):
    mongo.delete_all_taxes()
    taxes = pd.read_csv(taxes_file, engine='python')
    for tpl in taxes.itertuples():
        #mongo.insert_tax(name, rate):
        mongo.insert_tax(tpl[1], tpl[2])


def fill_products(products_file):
    mongo.delete_all_products()
    products = pd.read_csv(products_file, engine='python')
    # todo: fix reading csv so the columns can be in any order
    for tpl in products.itertuples():
        # mongo.insert_product(barcode, name, category, price, promoID, taxID )
        mongo.insert_product(tpl[1], tpl[2], tpl[3], tpl[4], tpl[5], tpl[6])



def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--products', '-p', type=str, default='', help='csv file containing product data')
    parser.add_argument('--taxes', '-t', type=str, default='', help='csv containing tax rates')
    parser.add_argument('--promos', '-pr', type=str, default='', help='csv containing promo info')
    args = parser.parse_args()

    if args.products:
        fill_products(args.products)
    if args.taxes:
        fill_taxes(args.taxes)
    if args.promos:
        fill_promos(args.promos)


if __name__ == '__main__':
    main()
    sys.exit()
