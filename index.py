from flask import Flask, redirect, render_template, url_for, request, jsonify
import db as db

app = Flask(__name__)


@app.errorhandler(404)
def RutaNoEncontrada(error):
    return render_template('error404.html'), 404



@app.route('/', methods= ["GET","POST"])
def Home():
    productos = db.getProducts()
    print(productos)
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        descripcion = request.form['descripcion']
        query = 'INSERT INTO productos(nombre, precio, stock, descripcion) VALUES ("{}",{},{},"{}");'.format(nombre, precio, stock, descripcion)
        print(query)
        db.executeQuery(query)
        return redirect('/')
    print(request.form)
    return render_template('home.html', products = productos)

@app.route('/clientes', methods = ["GET", "POST"])
def clientes():
    clientes = db.getClientes()
    return render_template('clientes.html', clientes = clientes)

@app.route('/delete/<id>', methods=["GET", "POST"])
def deleteProduct(id):
    query = "DELETE FROM productos WHERE id={};".format(id)
    db.executeQuery(query)
    return redirect('/')

@app.route('/deleteCliente/<id>', methods=["GET", "POST"])
def deleteClient(id):
    query = "DELETE FROM clientes WHERE id ={};".format(id)
    db.executeQuery(query)
    return redirect('/clientes')

@app.route('/edit/<id>', methods=["GET", "POST"])
def editProduct(id):
    producto = db.getOneProduct(id) 
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']
        stock = request.form['stock']
        descripcion = request.form['descripcion']
        query = 'UPDATE productos SET nombre="{}", precio={}, stock={}, descripcion="{}" where id={};'.format(nombre, precio, stock, descripcion, id)
        print(query)
        db.executeQuery(query)
        return redirect('/')
    return render_template('editP.html', producto=producto)

@app.route('/editCliente/<id>', methods=["GET", "POST"])
def editCliente(id):
    cliente = db.getCliente(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        email = request.form['email']
        telefono = request.form['telefono']
        query = 'UPDATE clientes SET nombre="{}", apellido="{}", email="{}", telefono="{}" where id={};'.format(nombre, apellido, email, telefono, id)
        print(query)
        db.executeQuery(query)
        return redirect('/clientes')
    return render_template('editCliente.html', cliente = cliente)
    

if __name__ == "__main__":
    app.run(port=80, debug=True, host='0.0.0.0')
