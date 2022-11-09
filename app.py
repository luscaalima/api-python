from flask import Flask, jsonify, request
from app_firebase import *
app=Flask(__name__)

link='https://lucas-firebase-default-rtdb.firebaseio.com'

firebase = Firebase(link)

@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify('LUCAS')

@app.route('/livros2',methods=['GET'])
def obter_livros2():
    return jsonify('LUCAS2')

@app.route('/criarCategoria',methods=['POST'])
def criar_categoria():
    body=request.get_json()
    print(body)
    print(type(body))
    print(type(jsonify('Lucas1')))
    firebase.criar_Categoria('parametro',body)
    return jsonify(body)



app.run(port=5000,host='localhost',debug=True)