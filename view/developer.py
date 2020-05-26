from  PyQt5.QtWidgets import *
from db import postgres


# docker start posdb
# docker ps

def create_products():
    create_products_table = """
        CREATE TABLE IF NOT EXISTS products (
        barcode SERIAL PRIMARY KEY,
        price NUMERIC(12,2),
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
        taxID SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        rate NUMERIC(12,6)
        )
        """
    postgres.execute_query(create_taxes_table)


def create_promos():
    create_promos_table = """
        CREATE TABLE IF NOT EXISTS promos (
        promoID SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        discount NUMERIC(12,6)
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


def insert_row(table, columns, values):

    assert len(columns) == len(values), ('Columns and values don\'t match')

    values_str = str(values)[1:-1]

    columns_str = str(columns)[1:-1].replace('\"', '').replace('\'', '')

    insert_row = ('INSERT INTO ' + table + ' (' + columns_str + ') '
                  + ' VALUES (' + values_str + ')')

    postgres.execute_query(insert_row)

def gui_create_products():
    create_products()

def gui_create_taxes():
    create_taxes()

def gui_create_promos():
    create_promos()

def gui_drop_products():
    drop_products()

def gui_drop_taxes():
    drop_taxes()

def gui_drop_promos():
    drop_promos()

if __name__ == '__main__':
    app = QApplication([])
    window = QWidget()
    layout = QVBoxLayout()

    button_create_products = QPushButton('create products')
    button_create_products.clicked.connect(gui_create_products)
    layout.addWidget(button_create_products)

    button_create_taxes = QPushButton('create taxes')
    button_create_taxes.clicked.connect(gui_create_taxes)
    layout.addWidget(button_create_taxes)

    button_create_promos = QPushButton('create promos')
    button_create_promos.clicked.connect(gui_create_promos)
    layout.addWidget(button_create_promos)

    button_drop_products = QPushButton('drop products')
    button_drop_products.clicked.connect(gui_drop_products)
    layout.addWidget(button_drop_products)

    button_drop_taxes = QPushButton('drop taxes')
    button_drop_taxes.clicked.connect(gui_drop_taxes)
    layout.addWidget(button_drop_taxes)

    button_drop_promos = QPushButton('drop promos')
    button_drop_promos.clicked.connect(gui_drop_promos)
    layout.addWidget(button_drop_promos)

    window.setLayout(layout)
    window.show()
    app.exec_()
