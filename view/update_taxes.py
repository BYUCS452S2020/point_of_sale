from  PyQt5.QtWidgets import *
from db import postgres

def get_taxes():
    query = """SELECT taxes.taxid, taxes.name, taxes.rate FROM taxes"""
    result = postgres.execute_read_query(query)
    return result

def change_tax():
    tax_index = combo_box_taxes.currentIndex()  # tax_index is
    tax_id = str(taxes[tax_index][0])  # tax_id is the DB key in taxes table
    new_tax_rate = str(line_edit_new_rate.text())
    line_edit_new_rate.selectAll()
    line_edit_new_rate.backspace()
    query = "UPDATE taxes SET rate = " + new_tax_rate + " WHERE taxid = " + tax_id
    #print(query)
    postgres.execute_query(query)

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

label_hello = QLabel()
layout.addWidget(label_hello)
label_hello.setText("Update tax info here")

combo_box_taxes = QComboBox()
taxes = get_taxes() #current tax rules in the DB
for tax_item in taxes:
    combo_box_taxes.addItem(tax_item[1])
layout.addWidget(combo_box_taxes)

line_edit_new_rate = QLineEdit()
layout.addWidget(line_edit_new_rate)

button_change_tax = QPushButton('update tax value')
button_change_tax.clicked.connect(change_tax)
layout.addWidget(button_change_tax)

window.setLayout(layout)
window.show()
app.exec_()


