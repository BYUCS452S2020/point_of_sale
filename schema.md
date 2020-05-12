#### Product (barcode_number, product_name, product_brand, product_category, product_cost, promo_id, tax_id)
Column descriptions/explanations
>- Primary key barcode_number (also thought of as product id)
>- Composite external key product_brand.product_name
>- Foreign key promo_id references Promo
>- Foreign key tax_id references Tax
>- product_cost is the dollar amount required to purchase one unit of product
>-product_name is the name of the product
>-product_brand is the name of the company that makes the product
>- product_category is the type of a product (fruit, vegetable, meat, etc)

Description of Table
>Product refers to an item that is sold and stocked at a store. When a transaction occurs, information regarding the product cost will be necessary and will come from this table.

How tables relate to each other
>promo_id binds the product to a given promotion that can be applied to the product, also referred to as a sale. 

>tax_id binds the product to the tax rate for said product. 



#### Tax (tax_id, tax_name, tax_rate)

Column descriptions/explanations
>- Primary key tax_id
>- Secondary external key tax_name
>- tax rate is the percentage of product cost that is added to cost of transaction.

Description of Table
>Tax refers to the information required to apply a tax to some product. 

How tables relate to each other
>The tax table is independent of the other tables in the database. It will be applied to a product though. Therefore, a given tax entry can relate to many products, but will have no knowledge of the products that it is related to. 


#### Promo (promo_id, promo_name, percent_discount)
Column descriptions/explanations
>- Primary key promo_id
>- Secondary external key promo_name
>- percent_discount is a percentage of some product_cost that is subtracted from the final transaction cost. 

Description of Table
>Promo is some sort of discount that can be applied to a product. 

How tables relate to each other
>The promo table is independent of the other tables in the database. It will be applied to a product though. Therefore, a given promotion relates to many products, but will have no knowledge of the products that it is related to. 

#### Evidence of Normalization
There are not instances of multi-valued dependencies within the database. This means that the database is in fourth normal form, which implies that it is in the three other normal forms as well. Attribute independence is defined by the primary key of a given row. Duplication of data is not required for attribute independence. 
