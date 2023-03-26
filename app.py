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

@app.route("/api/sql/awards")
def awards():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='root',
                                         password='Tony12345')
    
    sql_select_Query = "select * from awards"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'awards_index = ': row[0], 
            'awards_name = ': row[1],
            'awards_date  = ': row[2],
            'awards_entity  = ': row[3],
            'awards_winner  = ': row[4],
        })
        
    connection.close()
    return jsonify(datos_json)

@app.route("/api/sql/concentrate")
def concentrate():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='root',
                                         password='Tony12345')
    
    sql_select_Query = "select * from concentrate"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'concentrate_id = ': row[0], 
            'concentrate_name = ': row[1],
            'concentrate_strain  = ': row[2],
            'concentrate_thc = ': row[3],
            'concentrate_cbd  = ': row[4],
            'concentrate_dose  = ': row[5],
            'concentrate_type = ': row[6],
            'concentrate_effects  = ': row[7],
            'concentrate_flavors  = ': row[8],
            'concentrate_description  = ': row[9],
            'concentrate_id  = ': row[10]
        })
        
    connection.close()
    return jsonify(datos_json)

@app.route("/api/sql/creators")
def creators():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='root',
                                         password='Tony12345')
    
    sql_select_Query = "select * from creators"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'creators_index = ': row[0], 
            'creators_name = ': row[1],
            'creators_country  = ': row[2],
            'creators_mail = ': row[3],
            'creators_phone  = ': row[4],
            'creators_license  = ': row[5],
            'creators_strain  = ': row[6],
            'creators_lab  = ': row[7]
        })
        
    connection.close()
    return jsonify(datos_json)

@app.route("/api/sql/dispensary")
def dispensary():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='root',
                                         password='Tony12345')
    
    sql_select_Query = "select * from dispensary"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'dispensary_index = ': row[0], 
            'dispensary_name = ': row[1],
            'dispensary_state  = ': row[2],
            'dispensary_city = ': row[3],
            'dispensary_address  = ': row[4],
            'dispensary_phone  = ': row[5],
            'dispensary_mail  = ': row[6],
            'dispensary_strains  = ': row[7],
            'dispensary_products  = ': row[8]
        })
        
    connection.close()
    return jsonify(datos_json)

@app.route("/api/sql/strain")
def strain():
    connection = mysql.connector.connect(host='localhost',
                                         database='cannapi',
                                         user='root',
                                         password='Tony12345')
    
    sql_select_Query = "select * from strain"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    datos_json = []
    for row in records:
        datos_json.append({
            'strain_index = ': row[0], 
            'strain_name = ': row[1],
            'strain_type  = ': row[2],
            'strain_year = ': row[3],
            'strain_creator  = ': row[4],
            'strain_genes = ': row[5],
            'strain_thc  = ': row[6],
            'strain_cbd  = ': row[7],
            'strain_awards  = ': row[8],
            'strain_description = ': row[9],
            'strain_effects = ': row[10],
            'strain_flavors = ': row[11],
            'strain_id = ': row[12],
        })
        
    connection.close()
    return jsonify(datos_json)



