import csv

def write_table(filename, columns, table_arr):
    with open(filename, 'w') as f:
        table_writer = csv.writer(f)
        table_writer.writerow(columns)
        for arr in table_arr:
            table_writer.writerow(arr)


taxes = [('small tax', 0.01), ('medium tax', 0.1), ('big tax', 0.5), ('all tax', 1.0),
         ('no tax', 0.0), ('tea tax', 0.1776)]

promos = [('small promo', 0.99), ('medium promo', 0.9), ('big promo', 0.5), ('no promo', 1.0),
         ('free promo', 0.0), ('weird promo', 0.123)]

write_table('taxes.csv', ['name', 'rate'], taxes)
write_table('promos.csv', ['name', 'discount'], promos)
