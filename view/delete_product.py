from  PyQt5.QtWidgets import *
from db import postgres

def delete_prod():
    barcode = str(line_edit.text())
    line_edit.selectAll()
    line_edit.backspace()
    query = "delete from products where barcode = " + barcode
    postgres.execute_query(query)

app = QApplication([])
window = QWidget()
layout = QVBoxLayout()


label_hello = QLabel()
layout.addWidget(label_hello)
label_hello.setText("enter barcode of product to delete")

line_edit = QLineEdit()
layout.addWidget(line_edit)

button = QPushButton("delete product")
button.clicked.connect(delete_prod)
layout.addWidget(button)

window.setLayout(layout)
window.show()
app.exec_()


