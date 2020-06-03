from  PyQt5.QtWidgets import *
from PyQt5.QtCore import *
#from db import postgres

#enforce unique product, tax, and promo names
# add tax rules

def get_taxes():
    return "get_taxes()"

def get_promos():
    return "get_promos()"


def update_taxes_gui():
    tax_rate = line_edit_taxes.text()
    line_edit_taxes.clear()
    print("update taxes " + tax_rate)

def delete_product_gui():
    barcode = (delete_product_line_edit.text())
    delete_product_line_edit.clear()
    print("delete a product: " + str(barcode))

#todo: seperate db access from GUI.
def add_product_gui():
    tax_index = combo_box_taxes.currentIndex() #tax_index is
    tax_id = " " #str(taxes[tax_index][0]) #tax_id is the DB key in taxes table
    promo_index = combo_box_promos.currentIndex()
    promo_id = " "#str(promos[promo_index][0])
    product_name = str(line_edit_product_name.text())
    product_category = str(line_edit_product_category.text())
    product_price = str(line_edit_product_price.text())
    print("Add product. tax id=" + str(tax_id) + " promo id=" + str(promo_id) + " name="+ product_name + " price=" + product_price + " category=" + product_category)
    line_edit_product_name.clear()
    line_edit_product_category.clear()
    line_edit_product_price.clear()
    #label_new_barcode.setText("added product: " + product_name + " - barcode="+ str(result[0][0]))


##### GUI ######
app = QApplication([])
window = QWidget()
delete_product_layout = QVBoxLayout()
add_product_layout = QVBoxLayout()
update_taxes_layout = QVBoxLayout()
main_layout = QHBoxLayout()

##### Update taxes GUI #####
update_tax_hello = QLabel()
update_tax_hello.setText("Update Taxes")
update_taxes_layout.addWidget(update_tax_hello, 0, Qt.AlignTop)

combo_box_taxes = QComboBox()
combo_box_taxes.addItem("taxes 1")
combo_box_taxes.addItem("taxes 2")
update_taxes_layout.addWidget(combo_box_taxes, 0, Qt.AlignTop)

line_edit_taxes = QLineEdit()
line_edit_taxes.setPlaceholderText("new tax value")
update_taxes_layout.addWidget(line_edit_taxes)

taxes_button = QPushButton("update tax rate")
taxes_button.clicked.connect(update_taxes_gui)
update_taxes_layout.addWidget(taxes_button)


##### Delete product GUI #####
delete_product_hello = QLabel()
delete_product_layout.addWidget(delete_product_hello,0,Qt.AlignTop)
delete_product_hello.setText("Delete a Product")

delete_product_line_edit = QLineEdit()
delete_product_line_edit.setPlaceholderText("barcode of product")
delete_product_layout.addWidget(delete_product_line_edit,0,Qt.AlignTop)

delete_product_button = QPushButton("delete product")
delete_product_button.clicked.connect(delete_product_gui)
delete_product_layout.addWidget(delete_product_button,0,Qt.AlignBottom)

delete_product_layout.addSpacing(10)
delete_product_layout.addSpacing(10)
delete_product_layout.addSpacing(10)
delete_product_layout.addSpacing(10)

##### add product GUI #####
label_hello = QLabel()
add_product_layout.addWidget(label_hello)
label_hello.setText("Add New Product")

combo_box_taxes = QComboBox()
combo_box_taxes.addItem("tax 1")
combo_box_taxes.addItem("tax 2")
add_product_layout.addWidget(combo_box_taxes)

combo_box_promos = QComboBox()
combo_box_promos.addItem("promo 1")
combo_box_promos.addItem("promo 2")
add_product_layout.addWidget(combo_box_promos)

line_edit_product_name = QLineEdit()
line_edit_product_name.setPlaceholderText("name of product")
add_product_layout.addWidget(line_edit_product_name)

line_edit_product_category = QLineEdit()
line_edit_product_category.setPlaceholderText("name of category")
add_product_layout.addWidget(line_edit_product_category)

line_edit_product_price = QLineEdit()
line_edit_product_price.setPlaceholderText("product price")
add_product_layout.addWidget(line_edit_product_price)

label_new_barcode = QLabel()
label_new_barcode.setText("")
add_product_layout.addWidget(label_new_barcode)

#before allow user to submit, check the index of the 2 combo boxes to get the tax and promo forigen keys from combo_box_promos /taxes
button_submit_new_product = QPushButton('add product')
button_submit_new_product.clicked.connect(add_product_gui)
add_product_layout.addWidget(button_submit_new_product)

##### add layouts to the window #####
main_layout.addLayout(add_product_layout)
main_layout.addSpacing(40)
main_layout.addLayout(delete_product_layout)
main_layout.addSpacing(40)
main_layout.addLayout(update_taxes_layout)
window.setLayout(main_layout)
window.show()
app.exec_()
