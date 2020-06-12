import mysql.connector as py
con=py.connect(host="localhost",user="root",passwd="",database="IMS")
cur=con.cursor()
print("[1] PRESS 1 TO ADD NEW PRODUCT\n[2] PRESS 2 TO VIEW ALL PRODUCT\n[3] PRESS 3 TO REMOVE A PRODUCT")
u=int(input("\nENTER YOUR CHOICE:-"))
if u==1:
    ops='y'
    while ops=='y' or ops=='Y':
        print("\n\n>>>ENTER YOUR PRODUCT DETAIL<<<")
        pd=int(input('\nENTER PRODUCT ID:-      '))
        pn=input("ENTER PRODUCT NAME:-   ")
        pp=int(input('ENTER PUCHASE PRICE:-    '))
        sp=float(input('ENTER SALE PRICE:-    '))
        pq=int(input('ENTER PRODUCT QUANTITY:- '))
        q="insert into product(productid,productName,purchasePrice,salePrice,productQty) values(%d,'%s',%d,%f,%d)"%(pd,pn,pp,sp,pq)
        cur.execute(q)
        con.commit()
        print("ENTERY SUCCESSFULL....")
        ops=input('TO CONTINUE PRESS Y: ')
elif u==2:
    qe="SELECT * FROM product"
    cur.execute(qe)
    for x in cur:
        print(x)
elif u==3:
    s=int(input("enter the product id which you want to remove:-"))
    qr="DELETE FROM product WHERE productid=%d"%(s)
    cur.execute(qr)
    con.commit()
    print("done")
else:
    print('INCORRECT INPUT TRY AGAIN')
    
    
