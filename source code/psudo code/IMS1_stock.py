import mysql.connector as py
con=py.connect(host="localhost",user="root",passwd="",database="IMS")
cur=con.cursor()
print("\n[1] PRESS 1 TO UPDATE PRODUCT QUANTITY\n[2] PRESS 2 TO VIEW STOCK(productid,productQty)")
k=int(input("ENTER YOUR CHOICE:-"))
if k==1:
    l=int(input("ENTER THE PRODUCT ID WHICH YOU WANT TO UPDATE:-"))
    m=int(input("ENTERE THE UPDATED NEW PRODUCT QUANTITY:-"))
    q="UPDATE product SET productQty=%d WHERE productid=%d"%(m,l)
    cur.execute(q)
    con.commit()
    print("successfully updated....")
elif k==2:
    qe="SELECT productid,productQty FROM product"
    cur.execute(qe)
    for x in cur:
        print(x)
else:
    print("wrong input")
    
