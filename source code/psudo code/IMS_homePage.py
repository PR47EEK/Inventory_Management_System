import os
while True:
    print("\t\t\t ++---------------------------++")
    print("\t\t\t ++ INVENTORY                 ++")
    print("\t\t\t ||          MANAGEMENT       ||")
    print("\t\t\t ++                     SYSTEM++")
    print("\t\t\t ++---------------------------++")
    print("\t\t\t\t>>MAIN MENU<<\n\t\t\t\t=============\n")
    print("\n\n[1] PRESS 1 FOR MANAGE STOCK DETAILS\n[2] PRESS 2 FOR SALE DETAILS\n[3] PRESS 3 FOR MANAGE PRODUCTS\n[4] PRESS 4 FOR PROFIT DETAILS\n[5] PRESS 5 FOR EXIT\n")
    n=int(input("\n**ENTER YOUR CHOICE:-"))
    if n==1:
        import IMS1_stock
    elif n==2:
        import IMS2_sale
    elif n==3:
        import IMS3_manage
    elif n==4:
        import IMS4_profit
    elif n==5:
        print("     ~~~~~~~~~~~~~~@THANKS FOR USING OUR SERVICE@~~~~~~~~~~~")
        break
    else:
        print("  ##OOPS!! WRONG INPUT TRY AGAIN")
    
