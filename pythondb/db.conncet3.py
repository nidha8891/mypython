import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Paasword@123",
    database="animal"

)
cursor=mydb.cursor()
query="""
    insert into pets(age,gender,breed,location,price) value(12,"female","breed2","kozhikode",25000)
    insert into pets(age,gender,breed,lo)"""
cursor.execute(query)
mydb.commit()