import mysql.connector as py
con=py.connect(host="localhost",user="root",passwd="",database="IMS")
cur=con.cursor()
q="select product.productid,product.purchasePrice,sale.price,sale.date from product,sale where product.productid=sale.productID"
cur.execute(q)
for x in cur:
    print(x)
