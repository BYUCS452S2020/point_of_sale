from  PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from db import mongo

taxes = mongo.get_taxes() #will be updated everytime gui is refreshed.
promos = mongo.get_promos()
#updates combo boxes
def refresh_gui():
    promos = mongo.get_promos()
    global taxes
    taxes = mongo.get_taxes()
    promos = mongo.get_promos()
    tax_combo_box_taxes.clear()
    combo_box_taxes.clear()
    for t in taxes:
        tax_combo_box_taxes.addItem(t['name'] + ' ' + str(t['rate']))
        combo_box_taxes.addItem(t['name'] + ' ' + str(t['rate']))
    combo_box_promos.clear()
    for p in promos:
        combo_box_promos.addItem(p['name'])





#Gets called when the submit button is pressed for the update taxes part of the GUI
def update_taxes_gui():
    if len(line_edit_taxes.text()) == 0:
        return
    tax_rate = line_edit_taxes.text()
    tax_index = tax_combo_box_taxes.currentIndex()
    tax_name = taxes[tax_index]['name']
    line_edit_taxes.clear()
    mongo.update_tax(tax_name, tax_rate)
    refresh_gui()

#Gets called when the submit button is pressed for the delete product part of the GUI
def delete_product_gui():
    barcode = (delete_product_line_edit.text())
    delete_product_line_edit.clear()
    mongo.delete_product(barcode)

#Gets called when the submit button is pressed for the add product part of the GUI
def add_product_gui():
    barcode = line_edit_product_barcode.text()
    tax_index = combo_box_taxes.currentIndex() #tax_index is
    tax_name =  taxes[tax_index]['name']
    promo_index = combo_box_promos.currentIndex()
    promo_id = promos[promo_index]['name']
    product_name = line_edit_product_name.text()
    product_category = line_edit_product_category.text()
    product_price = line_edit_product_price.text()
    print("Add product. tax name=" + str(tax_name) + " promo id=" + str(promo_id) + " name="+ product_name + " price=" + product_price + " category=" + product_category)
    line_edit_product_name.clear()
    line_edit_product_category.clear()
    line_edit_product_price.clear()
    line_edit_product_barcode.clear()
    #label_new_barcode.setText("added product: " + product_name + " - barcode="+ str(result[0][0]))
    #mongo.insert_product(barcode, price, name, category, promoID, taxID)
    mongo.insert_product(barcode, product_price, product_name, product_category, promo_id, tax_name)


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

tax_combo_box_taxes = QComboBox()
tax_combo_box_taxes.addItem("taxes 1")
tax_combo_box_taxes.addItem("taxes 2")
update_taxes_layout.addWidget(tax_combo_box_taxes, 0, Qt.AlignTop)

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

line_edit_product_barcode = QLineEdit()
line_edit_product_barcode.setPlaceholderText("barcode")
add_product_layout.addWidget(line_edit_product_barcode)

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
refresh_gui()
app.exec_()
