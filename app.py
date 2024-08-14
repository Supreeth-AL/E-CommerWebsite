from flask import Flask
from flask_cors import CORS
from db import db
from admin_login import User_blueprint
from home import product_blueprint
from admin_dashboard import admin_dashboard_buleprint



app = Flask(__name__)
CORS(app)

#DB configaretion
username ='root'
password = '' #Admin_123
server = '127.0.0.1'
dbname = '/e_commerce_store'
userpass = 'mysql+pymysql://'+username+':'+password+'@'

app.config['SQLALCHEMY_DATABASE_URI'] = userpass + server + dbname
app.config['SQLALCHEMY_TRACK_MODIFICATION']=True

db.init_app(app)

#register blueprint
app.register_blueprint(User_blueprint)
app.register_blueprint(product_blueprint)
app.register_blueprint(admin_dashboard_buleprint)

@app.route('/server')
def serverStatus():
    return "server is up and running"


@app.route('/sum')
def sumStatus():
    a=2
    b=3
    return str(a+b)

@app.route('/exponential')
def exponential():
    a=5
    b=5
    return str(a**b)

@app.route('/multiplication')
def multiplication():
    a=500
    b=500
    return str(a*b)

if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True,port=8080)