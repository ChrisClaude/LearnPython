import mysql.connector
from mysql.connector import errorcode

# Connecting to MySQL Using Connector/Python
# This is the preferred way
"""
cnx = mysql.connector.connect(user='root', password='Cla@5027jesuschrist',
                              host='127.0.0.1',
                              database='pdoposts')
cnx.close()
"""

# It is also possible to create connection objects using the connection.MySQLConnection() class
"""
cnx = connection.MySQLConnection(user='root', password='Cla@5027jesuschrist',
                                 host='127.0.0.1',
                                 database='pdoposts')
cnx.close()
"""

# To handle connection errors, use the try statement and catch all errors using the errors.Error exception:
"""try:
    cnx = mysql.connector.connect(user='root',
                                  database='pdoposts')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()
"""

# Defining connection arguments in a dictionary and using the ** operator is another option
config = {
  'user': 'root',
  'password': 'Cla@5027jesuschrist',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True
}

cnx = mysql.connector.connect(**config)

cnx.close()
