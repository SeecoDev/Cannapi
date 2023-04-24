# Flask
from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
# JWT
import jwt
# SQLITE3
import sqlite3
# Otros
from  werkzeug.security import generate_password_hash, check_password_hash
import uuid
import json
from datetime import datetime, timedelta
from functools import wraps
from user_agents import parse


# Objeto de Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'BeethovenWeed'
# COnfiguracion de la base de datos con SQLalchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cannalite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

# Database ORMs
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    public_id = db.Column(db.String(50), unique = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(70), unique = True)
    password = db.Column(db.String(80))
    registerdate = db.Column(db.String(80))

class Log(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(70))
    logdate = db.Column(db.String(80))

# Funcion para obtener los datos del usuario
def get_user_info():
    user_agent = request.headers.get('User-Agent')
    user_agent_parsed = parse(user_agent)
    user_os = user_agent_parsed.os.family
    user_browser = user_agent_parsed.browser.family
    time_format = '%Y-%m-%d %H:%M:%S.%f'
    current_time = datetime.now()
    entry_time = current_time.strftime(time_format)
    return {
        'entry_time': entry_time,
        'browser': user_browser,
        'os': user_os
    }

# Verificardor del JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # El jwt se obtiene del header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # Return 401 si no hay token en el header
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401

        try:
            # decode del payload
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query\
                .filter_by(public_id = data['public_id'])\
                .first()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # return del usuario
        return  f(current_user, *args, **kwargs)
    return decorated


@app.route("/")
def main():
        return "<center><h1>CANNAPI CHAD API DEPLOY</h1></center><marquee>ADRIAN Y TONY</marquee>"

# Login
@app.route('/login', methods=['POST'])
def login():

    # Obtiene la info del usuario del request
    auth = request.form
    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="Login required !!"'}
        )

    user = User.query\
        .filter_by(email = auth.get('email'))\
        .first()

    if not user:
        # returns 401 if user does not exist
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        user_info = get_user_info()
        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds=120)),
            'user_os': user_info['os'],
            'user_browser': user_info['browser']
        },
            app.config['SECRET_KEY'])
        return make_response(jsonify({'token' : token.decode('UTF-8')}), 201)
    else:
        return make_response('Unable to verify', 403, {'WWW-Authenticate': 'Basic realm: "Authentication Failed "'})

#Register
@app.route('/register', methods = ['POST'])
def register():
    data = request.form
    name, email = data.get('name'), data.get('email')
    password = data.get('password')


    user = User.query\
        .filter_by(email = email)\
        .first()
    if not user:
        user = User(
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = generate_password_hash(password),
            registerdate = datetime.now()
        )
        log = Log(
            email = email,
            logdate = datetime.now())
        # insert user
        db.session.add(user)
        db.session.add(log)
        db.session.commit()
        return make_response('Successfully registered.', 201)
    else:
        # returns 202 if user already exists
        return make_response('User already exists. Please Log in.', 202)

#Autheticated
@app.route('/auth')
@token_required
def auth():
    return 'JWT is verified'

@app.route("/about")
def about():
    f = open('cannapi.json')
    display = json.load(f)
    return jsonify(display)


@app.route("/bye")
def bye():
    return "<h1> Recuerden fumar bandita</h1>"

@app.route("/awards")
@token_required
def awards():
    connection = mysql.connector.connect(host='DeuZzz.mysql.pythonanywhere-services.com',
                                         database='DeuZzz$cannapi',
                                     user='DeuZzz',
                                         password='AdrianYTony')
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

@app.route("/concentrate")
@token_required
def concentrate():
    connection = mysql.connector.connect(host='DeuZzz.mysql.pythonanywhere-services.com',
                                         database='DeuZzz$cannapi',
                                         user='DeuZzz',
                                         password='AdrianYTony')

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

@app.route("/creators")
@token_required
def creators():
    connection = mysql.connector.connect(host='DeuZzz.mysql.pythonanywhere-services.com',
                                         database='DeuZzz$cannapi',
                                         user='DeuZzz',
                                         password='AdrianYTony')

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

@app.route("/dispensary")
@token_required
def dispensary():

    connection = mysql.connector.connect(host='DeuZzz.mysql.pythonanywhere-services.com',
                                         database='DeuZzz$cannapi',
                                         user='DeuZzz',
                                         password='AdrianYTony')

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

@app.route("/strain")
@token_required
def strain():
    connection = sqlite3.connect("cannalite.db")
    cursor = connection.cursor()
    rows = cursor.execute("SELECT * from strains").fetchall()
    cursor.close()
    connection.close()
    return jsonify(rows)


