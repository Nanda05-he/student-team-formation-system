import oracledb

def get_connection():
    connection = oracledb.connect(
    user="system",
    password="dbms123",
    dsn="localhost/XE"
    )
    return connection
