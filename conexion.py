import mysql.connector
from mysql.connector import Error
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Cannabis',
                                         user='deuz',
                                         password='2Tostitos3!')

    mySql_Create_Table_Query = """CREATE TABLE Flor( 
                             idFlor int(11) NOT NULL,
                             nameFlor varchar(35) NOT NULL,
                             varietyFlor varchar(6) NOT NULL,
                             cultivoFlor varchar(7) NOT NULL,
                             thcFlor float NOT NULL,
                             cbdFLor float NOT NULL,
                             terpenesFlor float NOT NULL,
                             efectsFlor varchar(35) NOT NULL,
                             tasteFlor varchar(35) NOT NULL,
                             dateFlor date NOT NULL,
                             providerFlor varchar(35) NOT NULL,
                             colorsFlor varchar(35) NOT NULL,
                             awardsFlor varchar(35) NOT NULL,
                             priceFlor float NOT NULL,
                             weightFlor float NOT NULL,
                             PRIMARY KEY (idFlor)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Flor table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")