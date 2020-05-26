from  PyQt5.QtWidgets import *
from db import postgres

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

#todo: seperate db access from GUI.
def add_product():
    tax_index = combo_box_taxes.currentIndex() #tax_index is
    tax_id = str(taxes[tax_index][0]) #tax_id is the DB key in taxes table
    promo_index = combo_box_promos.currentIndex()
    promo_id = str(promos[promo_index][0])
    print("adding product:")
    product_name = str(line_edit_product_name.text())
    product_category = str(line_edit_product_category.text())
    product_price = str(line_edit_product_price.text())
    print("tax id=" + str(tax_id) + " promo id=" + str(promo_id) + " name ="+ product_name)
    query = "insert into products (barcode, price, name, category, promoid, taxid) values (DEFAULT," + product_price + ",'" + product_name + "','" + product_category + "'," + promo_id + "," + tax_id + ") returning barcode"
    print(query)
    result = postgres.execute_read_query(query)
    line_edit_product_name.selectAll()
    line_edit_product_name.backspace()
    line_edit_product_category.selectAll()
    line_edit_product_category.backspace()
    line_edit_product_price.selectAll()
    line_edit_product_price.backspace()
    label_new_barcode.setText("added product: " + product_name + " - barcode="+ str(result[0][0]))


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
label_prod_barcode.setText("product price")
layout.addWidget(label_prod_barcode)

line_edit_product_price = QLineEdit()
layout.addWidget(line_edit_product_price)

label_new_barcode = QLabel()
label_new_barcode.setText("")
layout.addWidget(label_new_barcode)

#before allow user to submit, check the index of the 2 combo boxes to get the tax and promo forigen keys from combo_box_promos /taxes
button_submit_new_product = QPushButton('add product')
button_submit_new_product.clicked.connect(add_product)
layout.addWidget(button_submit_new_product)


window.setLayout(layout)
window.show()
app.exec_()


