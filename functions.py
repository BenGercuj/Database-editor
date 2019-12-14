import mysql.connector

def sql_login(_host, _user, _pwd):
    _db = mysql.connector.connect(
            host=_host,
            user=_user,
            password=_pwd,
            use_pure=True
            )
    return _db

def sql_login_ssl(_host, _user, _pwd, _sslcaPath):
    _db = mysql.connector.connect(
            host=_host,
            user=_user,
            password=_pwd,
            ssl_ca=_sslcaPath,
            use_pure=True
            ) 
    return _db
    
def sql_login_sslxtra(_host, _user, _pwd, _sslcaPath, _sslcertPath, _sslkeyPath):
    _db = mysql.connector.connect(
            host=_host,
            user=_user,
            password=_pwd,
            ssl_ca=_sslcaPath,
            ssl_cert=_sslcertPath,
            ssl_key=_sslkeyPath,
            use_pure=True
            ) 
    return _db