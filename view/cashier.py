from  PyQt5.QtWidgets import *
from db import postgres


#TODO: fix this function so it works if there is no discount
def calculate_price(barcode):
    select_item = """
    SELECT products.price, taxes.rate, promos.discount, products.name FROM products
        JOIN taxes ON products.taxID = taxes.taxID
        JOIN promos ON products.promoID = promos.promoID
    WHERE products.barcode = """ + barcode

    result = postgres.execute_read_query(select_item)

    if len(result) > 1:
        raise Exception("Only one product should be returned")

    if len(result) == 0:
        raise Exception("no result returned for this barcode")

    # result looks like this: [(price, tax, discount, name)]
    print(result)
    price = result[0][0]
    rate = result[0][1]
    discount = result[0][2]
    name = result[0][3]
    discounted_price = price - (price * discount)
    tax = rate * discounted_price
    final_price = discounted_price + tax
    return final_price, name


#todo: add error checking and input validation
def gui_scan_item():
    barcode_number = line_edit_barcode.text()
    line_edit_barcode.selectAll()
    line_edit_barcode.backspace()

    final_price, name = calculate_price(barcode_number)
    print(final_price)
    print(name)
    label_calculations.setText(" ")
    label_final_price.setText(name + " - " + str(round(final_price, 2)))


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

button_create_products = QPushButton('scan item')
button_create_products.clicked.connect(gui_scan_item)
layout.addWidget(button_create_products)

line_edit_barcode = QLineEdit()
layout.addWidget(line_edit_barcode)

label_calculations = QLabel()
layout.addWidget(label_calculations)

label_final_price = QLabel()
layout.addWidget(label_final_price)

window.setLayout(layout)
window.show()
app.exec_()


