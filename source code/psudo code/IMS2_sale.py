ops="Y"
while ops=='y' or ops=='Y':
    import mysql.connector as py
    con=py.connect(host="localhost",user="root",passwd="",database="IMS")
    cur=con.cursor()
    sd=int(input('ENTER SALE ID:-'))
    pd=int(input('ENTER PRODUCT ID:-'))
    pr=float(input('ENTER SELLING PRICE:-'))
    da=input('enter your date yymmdd:- ')
    sq=int(input("ENTER SALE QUANTITY:-"))
    q="insert into sale(saleid,productID,price,date,saleQty) values(%d,%d,%f,'%s',%d)"%(sd,pd,pr,da,sq)
    cur.execute(q)
    con.commit()
    print("entery successfull...")
    ops=input("\n**TO CONTINUE PRESS Y:- ")
