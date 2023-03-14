from flask import Flask, jsonify
import json;
import mysql.connector;



app = Flask(__name__)



@app.route("/")
def main():
    return "<center><h1>HOLA ITE</h1></center><marquee>ADRIAN Y TONY CHAD</marquee>"

@app.route("/about")
def about():
    with open('cannapi.json',"r") as json:
        display = json.read()   
        return jsonify(display)


@app.route("/bye")
def adios():
    return "<h1> Recuerden fumar bandita</h1>"


@app.route("/api/sql/test")
def database():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannabis',
                                         user='root',
                                         password='Tony12345')
    
    sql_select_Query = "select * from flor"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    
    datos_json = []
    for row in records:
        datos_json.append({
            'idFlor = ': row[0], 
            'nameFlor = ': row[1],
            'varietyFlor  = ': row[2],
            'cultivoFlor  = ': row[3],
            'ctchFlor  = ': row[4],
            'cdbFlor  = ': row[5],
            'terpenesFlor  = ': row[6],
            'efectsFlor  = ': row[7],
            'tasteFlor  = ': row[8],
            'dateFlor  = ': row[9],
            'providerFlor  = ': row[10],
            'colorsFlor  = ': row[11],
            'awardsFlor  = ': row[12],
            'priceFlor  = ': row[13],
            'weightFlor  = ': row[14]
        })
        
    connection.close()
    return jsonify(datos_json)



