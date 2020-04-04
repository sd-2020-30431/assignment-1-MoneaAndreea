import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root", password="root", database = "wasteless")

mycursor = mydb.cursor()

def insert_into_database(name, quantity, calories, expiredate):
    try:
        sql_query = "INSERT INTO food (name, quantity, calories, expiredate) VALUES (%s, %s, %s, %s)"
        record_tuple = (name, quantity, calories, expiredate)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to insert record ")

def update_into_database(id, name):
    try:
        sql_query = "Update users set username = %s where iduser = %s"
        record_tuple = (name, id)
        mycursor.execute(sql_query, record_tuple)
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to update record ")

def delete_from_database(name):
    try:
        sql_query = "Delete from users where username = %s"
        mycursor.execute(sql_query, (name,))
        mydb.commit()
    except mysql.connector.Error as error:
        print("Failed to delete record ")
