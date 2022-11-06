from flask import Flask, jsonify, request

app=Flask(__name__)


@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify('LUCAS')

app.run(port=5000,host='localhost',debug=True)