import datetime
import mysql.connector as MySQL

def addwire(brand, length, gauge, bundles, dateof_purchase):
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        mySql_insert_query = """INSERT INTO wires (brand, length, gauge, bundles, dateof_purchase) 
                                    VALUES (%s, %s, %s, %s, %s) """

        record = (brand, length, gauge, bundles, dateof_purchase)
        cursor.execute(mySql_insert_query, record)
        con.commit()
        print("Record inserted successfully into wires table")
    except:
        print("Failed to insert into MySQL table")
    con.close()

def addswitch(brand, amp, pieces, dateof_purchase):
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        mySql_insert_query = """INSERT INTO switches (brand, amp, pieces, dateof_purchase) 
                                    VALUES (%s, %s, %s, %s) """

        record = (brand, amp, pieces, dateof_purchase)
        cursor.execute(mySql_insert_query, record)
        con.commit()
        print("Record inserted successfully into switches table")
    except:
        print("Failed to insert into MySQL table")
    con.close()
    



def showwire():
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        mySql_insert_query = "SELECT * FROM wires"
        cursor.execute(mySql_insert_query)
        records = cursor.fetchall()
        for row in records:
            print("Brand = ", row[0], )
            print("Length = ", row[1])
            print("Gauge  = ", row[2])
            print("Bundles  = ", row[3])
            print("Date Of Purchase  = ", row[4], "\n")
    except:
        print("Failed to display data in table wires")
    con.close()

def showswitch():
    params = {
    "host":"127.0.0.1", 
    "user":"root", 
    "password":"admin", 
    "database":"jkm"
    }
    try:
        con = MySQL.connect(**params)
        cursor = con.cursor()
        mySql_insert_query = "SELECT * FROM switches"
        cursor.execute(mySql_insert_query)
        records = cursor.fetchall()
        for row in records:
            print("Brand = ", row[0], )
            print("Current Rating = ", row[1])
            print("Pieces  = ", row[2])
            print("Date Of Purchase  = ", row[3], "\n")
    except:
        print("Failed to display data in table switches")
    con.close()

def main_menu():
    pass
