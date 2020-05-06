import psycopg2
from psycopg2 import OperationalError

import tkinter as tk
from tkinter import messagebox


def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")




def create_products():
    create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
        barcode INTEGER PRIMARY KEY,
        name TEXT NOT NULL, 
        category TEXT,
        promoID INTEGER,
        taxID INTEGER
        )
        """
    execute_query(connection, create_products_table)

def create_taxes():
    create_taxes_table = """
        CREATE TABLE IF NOT EXISTS taxes (
        taxID INTEGER PRIMARY KEY,
        name TEXT NOT NULL, 
        rate INTEGER
        )
        """
    execute_query(connection, create_taxes_table)

def create_promos():
    create_promos_table = """
        CREATE TABLE IF NOT EXISTS promos (
        promoID INTEGER PRIMARY KEY,
        name TEXT NOT NULL, 
        discount INTEGER
        )
        """
    execute_query(connection, create_promos_table)


def drop_products():
    drop_products_table = """ 
        DROP TABLE IF EXISTS products;
        """
    execute_query(connection, drop_products_table)

def drop_taxes():
    drop_products_table = """ 
        DROP TABLE IF EXISTS taxes;
        """
    execute_query(connection, drop_products_table)

def drop_promos():
    drop_products_table = """ 
        DROP TABLE IF EXISTS promos;
        """
    execute_query(connection, drop_products_table)    


connection = create_connection(
    "postgres", "postgres", "mysecretpassword", "localhost", "5432"
)

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


