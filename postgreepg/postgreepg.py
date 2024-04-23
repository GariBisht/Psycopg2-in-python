# How to connect PostgreSQL server with Python django
#comments by Garima Bisht
# Connecting postgreSQL to Python 


import psycopg2
#python driver  library used in postgreSQL
import config import config


# connection = psycopg2.connect(
    #host = "localhost" , port="5432" , database ="master" user= "postgres" , password="12345" )

# function
def connect():
  # object have no value 

    connection = None 
    try:
       params = config()
       print('Connecting to the postgreSQL database ....')
       connection = psycopg2.connect(**params)

     #create a cursor 
       crsr = connection.cursor()

       print('Welcome PostgreSQL database version :')

       crsr.execute('SELECT version()')
       db_version = crsr.fetchone()
       print(db_version)    #print db version variable 
       crsr.close()
    except(Exception , psycopg2.DatabaseError) as error:
     print(error)
    finally:
     if connection is not None:
        connection.close()
        print('Database connection terminated.')

if _name_ = "_main_":
    connect()


    #for run python postgreepg.py 
