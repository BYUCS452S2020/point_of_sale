import argparse
from db import postgres
from view import developer
import pandas as pd
import sys

def fill_promos(promos_file):
    promos = pd.read_csv(promos_file, engine='python')

    developer.drop_promos()
    developer.create_promos()
    insert_rows(promos, 'promos', ['name', 'discount'])

def fill_taxes(taxes_file):
    taxes = pd.read_csv(taxes_file, engine='python')

    developer.drop_taxes()
    developer.create_taxes()
    insert_rows(taxes, 'taxes', ['name', 'rate'])

def fill_products(products_file):
    products = pd.read_csv(products_file, engine='python')

    developer.drop_products()
    developer.create_products()
    insert_rows(products, 'products', ['price', 'name', 'category', 'promoID', 'taxID'], offset=2)

def insert_rows(df, table, columns, offset=1):
    for tpl in df.itertuples():
        print(tpl)
        new_row = []
        for item in tpl[offset:]:
            new_row.append(item)
        developer.insert_row(table, columns, new_row)

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
