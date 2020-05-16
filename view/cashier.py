import tkinter as tk
from db import postgres

def calculate_price(barcode):

    select_item = """
    SELECT products.price, taxes.rate, promos.discount FROM product
        JOIN taxes ON products.taxID = taxes.taxID
        JOIN promos ON products.promoID = promos.promoID
    WHERE products.barcode = """ + barcode

    result = postgres.execute_query(select_item)

    if len(result) > 1:
        raise Exception("Only one product should be returned")

    final_price = result.price * result.rate * result.discount

    return final_price
