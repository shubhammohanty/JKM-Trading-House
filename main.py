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
    
