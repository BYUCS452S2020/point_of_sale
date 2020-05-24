from  PyQt5.QtWidgets import *
from db import postgres

#don't let manager add a product unless the taxid is valid. this is solved with drop down list
#enforce unique product, tax, and promo names
# add tax rules

def get_taxes():
    query = """SELECT taxes.taxid, taxes.name, taxes.rate FROM taxes"""
    result = postgres.execute_read_query(query)
    return result

def get_promos():
    query = """SELECT promoid, name, discount FROM promos"""
    result = postgres.execute_read_query(query)
    return result

#todo: db access function
def add_product():
    tax_index = combo_box_taxes.currentIndex() #tax_index is
    tax_id = taxes[tax_index][0] #tax_id is the DB key in taxes table
    promo_index = combo_box_promos.currentIndex()
    promo_id = promos[promo_index][0]
    print("adding product:")
    product_name = line_edit_product_name.text()
    product_category = line_edit_product_category.text()
    product_barcode = line_edit_product_barcode.text()
    print("tax id=" + str(tax_id) + " promo id=" + str(promo_id) + " name ="+ product_name)

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()


label_hello = QLabel()
layout.addWidget(label_hello)
label_hello.setText("Select tax and promo rules")

combo_box_taxes = QComboBox()
taxes = get_taxes() #current tax rules in the DB
for tax_item in taxes:
    combo_box_taxes.addItem(tax_item[1] + " " + str(tax_item[2]))
layout.addWidget(combo_box_taxes)

combo_box_promos = QComboBox()
promos = get_promos()
for promo_item in promos:
    combo_box_promos.addItem(promo_item[1])
layout.addWidget(combo_box_promos)

label_prod_name = QLabel()
layout.addWidget(label_prod_name)
label_prod_name.setText("name of product")

line_edit_product_name = QLineEdit()
layout.addWidget(line_edit_product_name)

label_prod_category = QLabel()
label_prod_category.setText("name of category")
layout.addWidget(label_prod_category)

line_edit_product_category = QLineEdit()
layout.addWidget(line_edit_product_category)

label_prod_barcode = QLabel()
label_prod_barcode.setText("product barcode")
layout.addWidget(label_prod_barcode)

line_edit_product_barcode = QLineEdit()
layout.addWidget(line_edit_product_barcode)

#before allow user to submit, check the index of the 2 combo boxes to get the tax and promo forigen keys from combo_box_promos /taxes
button_submit_new_product = QPushButton('add product')
button_submit_new_product.clicked.connect(add_product)
layout.addWidget(button_submit_new_product)


window.setLayout(layout)
window.show()
app.exec_()


