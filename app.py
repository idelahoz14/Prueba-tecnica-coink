from crypt import methods
from flask import Flask, app, request
from flask.templating import render_template
from db import get_db
from werkzeug.utils import redirect
from flask.helpers import url_for
from flask import jsonify
import logging

# Config
app = Flask(__name__)
app.secret_key = 'mysecretkey'

# Routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/add_user", methods=['POST'])
def add_user():
    if request.method == 'POST':
        fullName = request.form['fullName']
        Email = request.form['Email']
        Ciudad = request.form['Ciudad']
        
        #sqlite consult
        cur = get_db().cursor()
        cur.execute('INSERT INTO  Users (fullName, Email, Ciudad) VALUES (?, ?, ?)',
        (fullName, Email, Ciudad))
        get_db().commit()

        logging.basicConfig(filename='registro.log')

        return redirect(url_for('index'))

@app.route("/registros")
def registros():
    cur = get_db().cursor()
    cur.execute('SELECT * FROM Users')
    data = cur.fetchall()

    return render_template('/registros.html', users = data)

# Elimina todos los registros de la tabla
@app.route("/delete_user", methods=['DELETE'])
def delete_user():
    cur = get_db().cursor()
    cur.execute('DELETE FROM Users')
    get_db().commit()
    return 'Eliminado'

if __name__ == '__main__':
    app.run(port = 3000, debug = True)
