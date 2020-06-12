import mysql.connector as my

con=my.connect(
  host="localhost",
  user="root",
  passwd="",
  database="IMS"
)
cur=con.cursor()
q="CREATE TABLE product(productid INT,productName VARCHAR(30),purchasePrice int,salePrice decimal(8,2),productQty int,PRIMARY KEY(productid))"
cur.execute(q)
qr="CREATE TABLE sale(saleid int,productID INT,price decimal(8,2),date DATE,saleQty int, FOREIGN KEY (productID) REFERENCES product(productid))"
cur.execute(qr)
q1="SHOW TABLES"
cur.execute(q1)

for x in cur:
    print(x)

