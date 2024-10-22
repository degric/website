import mysql.connector as mariadb

conn = mariadb.connect(host="localhost",
    user="max",
    password="hola",
    database="mieleria")

def executeQuery(query):

    try: 
        with conn.cursor() as cur:
            cur.execute(query)
            conn.commit()
    except Exception as e:
        print(f"Error: {e}")



def getProducts():
    try: 
        with conn.cursor() as cur:
            query = 'SELECT * FROM productos;'
            cur.execute(query)
            products = cur.fetchall()
            return products
    except mariadb.Error as error: 
        print("Error: {}".format(error))

def getOneProduct(id):
    try: 
        with conn.cursor() as cur:
            query = 'SELECT * FROM productos WHERE id={};'.format(id)
            cur.execute(query)
            product = cur.fetchone()
            print(product)
            return product
    except mariadb.Error as error:
        print("Error: {}".format(error))

def getClientes():
    try: 
        with conn.cursor() as cur:
            query = 'SELECT * FROM clientes;'
            cur.execute(query)
            clientes = cur.fetchall()
            return clientes
    except mariadb.Error as error: 
        print("Error: {}".format(error))

def getCliente(id):
    try:
        with conn.cursor() as cur:
            query = 'SELECT * FROM clientes WHERE id={};'.format(id)
            cur.execute(query)
            cliente = cur.fetchone()
            return cliente
    except mariadb.Error as error:
        print("Error: {}".format(error))