import mysql.connector

def create_db():
    # making connection
    con = mysql.connector.connect(host="localhost", user="root", passwd="Afran@1601", database="car_inventory")
    cur = con.cursor()
    cur.execute("CREATE DATABASE if not exists CAR_INVENTORY;")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), email VARCHAR(40), gender VARCHAR(5), contact VARCHAR(10), dob VARCHAR(15), doj VARCHAR(15), pass VARCHAR(30), utype VARCHAR(20), address VARCHAR(50), salary VARCHAR(10))")
    con.commit()

create_db()

