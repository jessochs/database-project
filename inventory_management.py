import sqlite3

# connection to database
connect = sqlite3.connect('inventory2.db')

# curser
curse = connect.cursor()

# create the tables
curse.execute("""CREATE TABLE brands (
              brand_id int,
              brand_name text
)""")

curse.execute("""CREATE TABLE products(
              product_id int,
              product_name text,
              manufacturer text,
              brand_id int
)""")

curse.execute("""CREATE TABLE stock(
              amount_in_stock int,
              product_id int
)""")

curse.execute("""CREATE TABLE sales(
              sales_amount int,
              product_id int
)""")

# add values to the brands table

many_brands = [
                (111, 'Billabong'),     
                (112, 'RSQ'),     
                (113, 'Vans'), 
                (114, 'Santa Cruz'), 
                (115, 'The North Face'), 
                (116, 'Salty Crew'),
            ]



curse.executemany("INSERT INTO brands VALUES (?, ?)", many_brands)
connect.commit()

# add values to the products table
many_products = [
                    (2000, 'Oversized Tee', 'Authentic Brands Group', 111), 
                    (2001, 'Mens Loose Cargo Pants', 'Tillys', 112), 
                    (2002, 'Old Skool Shoes', 'VF Corporation', 113), 
                    (2003, 'Santa Cruz Mens Tee', 'NHS', 114), 
                    (2004, 'Places We Love Hoodie', 'VF Corporations', 115), 
                    (2005, 'Hut Premium Mens Tee', 'Globe', 116), 
                    (2006, 'Authentic Black Shoes', 'VF Corporations', 113), 
                    (2007, 'Wild and Free Tee', 'Tillys', 112), 
                    (2008, 'Mens Button Down Shirt', 'Authentic Brands Group', 111), 
                    (2009, '3-pack Mens Crew Socks', 'Globe', 116),
                ]

curse.executemany("INSERT INTO products VALUES (?, ?, ?, ?)", many_products)

# add products to the stock table

many_in_stock = [
                    (150, 2000), 
                    (200, 2001), 
                    (700, 2002), 
                    (100, 2003), 
                    (115, 2004), 
                    (40, 2005), 
                    (280, 2006), 
                    (175, 2007), 
                    (120, 2008), 
                    (750, 2009),
                ]

curse.executemany("INSERT INTO stock VALUES (?, ?)", many_in_stock)

# add values to the sales table

many_sales = [
                    (76, 2000), 
                    (139, 2001), 
                    (541, 2002), 
                    (62, 2003), 
                    (109, 2004), 
                    (27, 2005), 
                    (254, 2006), 
                    (161, 2007), 
                    (88, 2008), 
                    (639, 2009),
                ]

curse.executemany("INSERT INTO sales VALUES (?, ?)", many_sales)
connect.commit()

# query all data entered

curse.execute("SELECT * FROM brands")
print("")
print("Brand Data (brand_id, brand_name)")
print(" ")
items1 =curse.fetchall()
for item in items1:
    print(item) 

curse.execute("SELECT * FROM products")
print("")
print("Product Data (product_id, product_name, manufacturer, brand_id)")
print(" ")
items2 =curse.fetchall()
for item in items2:
    print(item)  

curse.execute("SELECT * FROM stock")
print("")
print("Stock Data (amount_in_stock, product_id)")
print(" ")
items3 =curse.fetchall()
for item in items3:
    print(item) 

curse.execute("SELECT * FROM sales")
print("")
print("Sales Data (sales_amount, product_id)")
print(" ")
items4 =curse.fetchall()
for item in items4:
    print(item) 

connect.commit()

# I want to update the sales table since more products have been sold
    
curse.execute("""UPDATE sales SET sales_amount = 575
              WHERE product_id = 2002 """)

curse.execute("""UPDATE sales SET sales_amount = 115
              WHERE product_id = 2004 """)

curse.execute("""UPDATE sales SET sales_amount = 270
              WHERE product_id = 2006 """)

curse.execute("""UPDATE sales SET sales_amount = 90
              WHERE product_id = 2008 """)

connect.commit()

# print the change

curse.execute("SELECT *  FROM sales")
print("")
print("Changes to sales:")
changes = curse.fetchall()
for change in changes:
    print(change)

# one product is now out of stock, so it needs to be deleted from the stock table
# I want to keep it everywhere else, though, because I still records of how much was sold
# and that it was a product that we carried

curse.execute("DELETE FROM stock WHERE product_id = 2004")
# connect.commit()

# check the table to make sure 2004 doesn't show up
curse.execute("SELECT * FROM stock")
print('')
print("Delete product_id 2004")
deleted = curse.fetchall()
for d in deleted:
    print(d)

# AGGREGATE FUNCTIONS
    

curse.execute("SELECT SUM(sales_amount) FROM sales")

result = curse.fetchone()
print(f"The total amount of sales is: {result}")

curse.execute("SELECT * FROM stock")
curse.execute("SELECT MIN(amount_in_stock) FROM stock")

stock_min = curse.fetchone()
print(f"The minimum amount in stock is:{stock_min} ")


# JOIN

curse.execute("""SELECT products.product_id, products.product_name, stock.amount_in_stock
                FROM products
                INNER JOIN stock
                ON products.product_id = stock.product_id; """)
show_join = curse.fetchall()
print("")
print("Results from the JOIN:")
for j in show_join:
    print(j)

connect.commit()
connect.close()