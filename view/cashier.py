from  PyQt5.QtWidgets import *
from db import mongo


#TODO: fix this function so it works if there is no discount
def calculate_price(barcode):
    result = mongo.get_product(barcode)
    print(result)
    tax_name = result[0]['taxID']
    promo_name = result[0]['promoID']
    print(tax_name)
    # result looks like this: [(price, tax, discount, name)]
    price = result[0]['price']
    print(price)
    rate = mongo.get_one_tax(tax_name)
    print(rate)
    discount = mongo.get_one_promo(promo_name)
    name = result[0]['name']
    discounted_price = price - (price * discount)
    tax = rate * discounted_price
    final_price = discounted_price + tax
    return final_price, name


#todo: add error checking and input validation
def gui_scan_item():
    barcode_number = line_edit_barcode.text()
    line_edit_barcode.clear()
    calculate_price(barcode_number)
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


