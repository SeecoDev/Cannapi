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
def bye():
    return "<h1> Recuerden fumar bandita</h1>"

@app.route("/api/sql/flor")
def flor():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='deuz',
                                         password='2Tostitos3!')
    
    sql_select_Query = "select * from flor"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'florId = ': row[0], 
            'florNombre = ': row[1],
            'florTipo  = ': row[2],
            'florCreacion  = ': row[3],
            'florCreador  = ': row[4],
            'florPadres  = ': row[5],
            'florTHC  = ': row[6],
            'florCBD  = ': row[7],
            'florPremios  = ': row[8],
            'florDescripcion  = ': row[9],
            'florEfectos  = ': row[10],
            'florSabores  = ': row[11]
        })
        
    connection.close()
    return jsonify(datos_json)

@app.route("/api/sql/concentrado")
def concentrado():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='deuz',
                                         password='2Tostitos3!')
    
    sql_select_Query = "select * from concentrado"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'concentradoId = ': row[0], 
            'concentradoNombre = ': row[1],
            'concentradoStrain  = ': row[2],
            'concentradoTHC = ': row[3],
            'concentradoCBD  = ': row[4],
            'concentradoDosis  = ': row[5],
            'concentradoTipo = ': row[6],
            'concentradoEfectos  = ': row[7],
            'concentradoSabores  = ': row[8],
            'concentradoDescripcion  = ': row[9]
        })
        
    connection.close()
    return jsonify(datos_json)

@app.route("/api/sql/premios")
def concentrado():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='deuz',
                                         password='2Tostitos3!')
    
    sql_select_Query = "select * from premios"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'premiosId = ': row[0], 
            'premiosNombre = ': row[1],
            'premiosFecha  = ': row[2],
            'premiosEntidad = ': row[3],
            'premiosGanados  = ': row[4]
        })
        
    connection.close()
    return jsonify(datos_json)
    


