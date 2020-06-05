from pymongo import MongoClient
client = MongoClient()
client = MongoClient('192.168.99.100', 27017)
db = client['pymongo_test']
test_products = db.test_products


def insert_product(barcode, name, category, price, promoID, taxID ):
    data = {
        'barcode':barcode,
        'price':price,
        'name': name,
        'category': category,
        'promoID':promoID,
        'taxID':taxID
    }
    result = test_products.insert_one(data)
    print(result)

#insert_product(barcode, name, category, price, promoID, taxID )
#insert_product(12345, "apples", "produce", .59, 0, 0)
