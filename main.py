from datetime import date
import mysql.connector as MySQL

def main_menu():
    pass

#-----------------------------------------Owner Side--------------------------------------------
def owner_menu():
    print(""" 
    1) Show Stock
    2) Show Orders
    3) Add Wires
    4) Add Switches
    5) Add Doorbells""")
    choice = int(input("Enter the corresponding menu number to proceed: "))
    if choice == 1:
        print(" ")
        showstockowner()
    elif choice ==2:
        print(" ")
        showorders()
    elif choice == 3:
        print(" ")
        addwire()
    elif choice == 4:
        print(" ")
        addswitch()
    elif choice ==5:
        print(" ")
        addbell()
    else:
        print("Invalid Input. Kindly enter a correct input value.")
    

def addwire():
    brand = input("Enter the brand of wire: ")
    length = int(input("Enter the length of the wire(in ft): "))
    gauge = int(input("Enter the gauge of wire: "))
    bundles = int(input("Enter the bundles of wire: "))
    dateof_purchase = date.today()
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)              #connection estalishment
        cursor = con.cursor()
        mySql_insert_query = 'insert into wires values' + '(' + '"' + str(brand) + '"' + ',' + str(length) + ',' + str(gauge) + ',' + str(bundles) + ',' + '"' + str(dateof_purchase) + '"' + ')'

        cursor.execute(mySql_insert_query)         #query execution
        con.commit()
        print("Record inserted successfully into wires table")
    except:
        print("Failed to insert into MySQL table")
    con.close()

def addswitch():
    brand = input("Enter the brand of switch: ")
    amp = int(input("Enter the amperage of the switch: "))
    pieces = int(input("Enter the no. of pieces: "))
    dateof_purchase = date.today()
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        mySql_insert_query = 'insert into switches values' + '(' + '"' + str(brand) + '"' + ',' + str(amp) + ',' + str(pieces) + ',' + '"' + str(dateof_purchase) + '"' + ')'

        cursor.execute(mySql_insert_query)
        con.commit()
        print("Record inserted successfully into switches table")
    except:
        print("Failed to insert into MySQL table")
    con.close()
    
def addbell():
    brand = input("Enter the brand of bell: ")
    power = input("Enter if bell is AC or battery powered: ")
    quantity = int(input("Enter the quantity: "))
    dateof_purchase = date.today()
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)              #connection estalishment
        cursor = con.cursor()
        mySql_insert_query = 'insert into bells values' + '(' + '"' + str(brand) + '"' + ',' + '"' + str(power) + '"' + ',' + str(quantity) + ',' + '"' + str(dateof_purchase) + '"' + ')'
        cursor.execute(mySql_insert_query)         #query execution
        con.commit()
        print("Record inserted successfully into wires table")
    except:
        print("Failed to insert into MySQL table")
    con.close()

def showstockowner():
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM wires")
        wirestock = cursor.fetchall()
        print("-------------------------WIRES STOCK-------------------------------------")
        for row in wirestock:
            print("Brand = ", row[0], )
            print("Length = ", row[1])
            print("Gauge  = ", row[2])
            print("Bundles  = ", row[3])
            print("Date Of Purchase  = ", row[4], "\n")

        cursor.execute("SELECT * FROM switches")
        switchstock = cursor.fetchall()
        print("--------------------------SWITCHES STOCK-------------------------------")
        for row in switchstock:
            print("Brand = ", row[0], )
            print("Amp = ", row[1])
            print("Pieces  = ", row[2])
            print("Date Of Purchase  = ", row[3], "\n")

        cursor.execute("SELECT * FROM bells")
        bellstock = cursor.fetchall()
        print("--------------------------BELLS STOCK---------------------------------")
        for row in bellstock:
            print("Brand = ", row[0])
            print("Power = ", row[1])
            print("Quantity  = ", row[2])
            print("Date Of Purchase  = ", row[3], "\n") 
       
    except:
        print("Failed to display data in stock")
    con.close()

def showorders():
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM orders where status!='confirmed'")
        orders = cursor.fetchall()
        print("All pending orders:")
        for i in orders:
            print(i)
        print(" ")
        while True:
            choice = input("Enter the OrderID for which you want to confirm order: ")
            query = 'update orders set status="confirmed" where ID=' + choice
            cursor.execute(query)
            con.commit()
            print("Order confirmed for ID ",choice)
            cont = input("Enter q or Q to exit and any othr key to add more: ")
            if cont == 'q' or cont == 'Q':
                print("Exiting...")
                print(" ")
                break
    except:
            print("there is some error")
    con.close()





#-----------------------------------------Client Side--------------------------------------------
def showitems():
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM wires")
        wirestock = cursor.fetchall()
        print("-------------------------WIRES STOCK-------------------------------------")
        for row in wirestock:
            print("Brand = ", row[0])
            print("Length = ", row[1])
            print("Gauge  = ", row[2])

        cursor.execute("SELECT * FROM switches")
        switchstock = cursor.fetchall()
        print("--------------------------SWITCHES STOCK-------------------------------")
        for row in switchstock:
            print("Brand = ", row[0], )
            print("Length = ", row[1])
            print("Gauge  = ", row[2])

        cursor.execute("SELECT * FROM bells")
        bellstock = cursor.fetchall()
        print("--------------------------BELLS STOCK---------------------------------")
        for row in bellstock:
            print("Brand = ", row[0])
            print("Power = ", row[1])
    except:
        print("Failed to display data in table stock")
    con.close()

def createorder():
    pass

def client_menu():
    pass

