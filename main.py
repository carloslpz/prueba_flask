from flask import Flask
import jsonize as js

app = Flask(__name__)

@app.route('/sepomex/estados')
def return_estados():
    return js.get_all_estados()

@app.route('/sepomex/municipios')
def return_municipios():
    return js.get_all_municipios()

@app.route('/sepomex/colonias')
def return_colonias():
    return js.get_all_colonias()

@app.route('/sepomex/admin_postal')
def return_admin_postal():
    return js.get_all_admin_postal()

@app.route('/sepomex/colonias/<cp>')
def return_colonias_cp(cp):
    return js.get_colonias_cp(cp)










app.run(debug = True)

