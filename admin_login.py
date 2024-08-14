from flask import Blueprint,request
from classModules.userClass import objUsers
import hashlib

User_blueprint = Blueprint('users_blueprint',__name__)
@User_blueprint.route('/validate-cred',methods=['POST'])
def chkAdminUser():
    
    username = request.form['username']
    password = request.form['password']
    
    if not username and not password:
        return '[{"errMsg":1,"message":"InvalidCredentials"}]'
    
    #Encrypt password to sha256
    encPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()
    
    resultvalue = objUsers.validateCred(username,encPassword)
    
    if resultvalue == 0:
        return '[{"errFlag":1,"message":"InvalidCredentials"}]'
    else:
        return resultvalue