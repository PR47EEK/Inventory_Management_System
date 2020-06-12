import mysql.connector as my

con=my.connect(host="localhost",user="root",passwd="")

cur=con.cursor()
q="CREATE DATABASE IMS"
cur.execute(q)
qr="SHOW DATABASES"
cur.execute(qr)

for x in cur:
  print(x) 
print("DONE..........")
