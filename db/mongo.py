from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client['pos']
products = db.products
taxes = db.taxes
promos = db.promos

def insert_product(barcode, price, name, category, promoID, taxID ):
    data = {
        'barcode':barcode,
        'price':price,
        'name': name,
        'category': category,
        'promoID':promoID,
        'taxID':taxID
    }
    result = products.insert_one(data)

def insert_tax(name, rate):
    data = {
        'name': name,
        'rate': rate
    }
    taxes.insert_one(data)

def insert_promo(name, discount):
    data = {
        'name':name,
        'discount': discount
    }
    promos.insert_one(data)

def delete_all_products():
    db.products.remove({})

def delete_all_promos():
    db.promos.remove({})

def delete_all_taxes():
    db.taxes.remove({})
