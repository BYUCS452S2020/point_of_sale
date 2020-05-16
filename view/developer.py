import tkinter as tk
from db import postgres

def create_products():
    create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
        barcode INTEGER PRIMARY KEY,
        price NUMERIC(2),
        name TEXT NOT NULL, 
        category TEXT,
        promoID INTEGER,
        taxID INTEGER
        )
        """
    postgres.execute_query(create_products_table)

def create_taxes():
    create_taxes_table = """
        CREATE TABLE IF NOT EXISTS taxes (
        taxID INTEGER PRIMARY KEY,
        name TEXT NOT NULL, 
        rate INTEGER
        )
        """
    postgres.execute_query(create_taxes_table)

def create_promos():
    create_promos_table = """
        CREATE TABLE IF NOT EXISTS promos (
        promoID INTEGER PRIMARY KEY,
        name TEXT NOT NULL, 
        discount INTEGER
        )
        """
    postgres.execute_query(create_promos_table)


def drop_products():
    drop_products_table = """ 
        DROP TABLE IF EXISTS products;
        """
    postgres.execute_query(drop_products_table)

def drop_taxes():
    drop_products_table = """ 
        DROP TABLE IF EXISTS taxes;
        """
    postgres.execute_query(drop_products_table)

def drop_promos():
    drop_products_table = """ 
        DROP TABLE IF EXISTS promos;
        """
    postgres.execute_query(drop_products_table)



window = tk.Tk()
window.title("create and drop tables")

my_label = tk.Label(text="create and drop tables ", width=40)
my_label.pack()

create_products_button = tk.Button(text="create table products", command=create_products)
create_products_button.pack()

create_taxes_button = tk.Button(text="create table taxes", command=create_taxes)
create_taxes_button.pack()

create_promos_button = tk.Button(text="create table promos", command=create_promos)
create_promos_button.pack()

drop_products_button = tk.Button(text="drop table products", command=drop_products)
drop_products_button.pack()

drop_taxes_button = tk.Button(text="drop table taxes", command=drop_taxes)
drop_taxes_button.pack()

drop_promos_button = tk.Button(text="drop table promos", command=drop_promos)
drop_promos_button.pack()

window.mainloop()
