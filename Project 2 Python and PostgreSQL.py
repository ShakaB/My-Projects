#Project 2 Python and PostgreSQL

import psycopg2
from tabulate import tabulate

print("Beginning")

# Change the credentials and the name of the database
# create table student(id integer, name varchar(10), primary key(id))

con = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="********")

print(con)

#For isolation: SERIALIZABLE It makes sure changes happen one after the other in the event mulitple users
#Are connecting and updating the system at the same time 
con.set_isolation_level(3)

#For atomicity. Specifics whether changes made to the database is committed or not 
con.autocommit = False

try:
    cur = con.cursor()
    # QUERY The product p1 is deleted from Product and Stock
    cur.execute("DELETE FROM Stock WHERE prod_id = 'p1'; DELETE FROM Product WHERE prod_id = 'p1';")

except (Exception, psycopg2.DatabaseError) as err:
    print(err)
    print("Transactions could not be completed so database will be rolled back before start of transactions")
    con.rollback()
finally:
    if con:
        con.commit()
        cur.close
        con.close
        print("PostgreSQL connection is now closed")

print("End")
