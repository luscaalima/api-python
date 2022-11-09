from flask import Flask, jsonify, request
from app_firebase import *
app=Flask(__name__)

link='https://lucas-firebase-default-rtdb.firebaseio.com'

firebase = Firebase(link)


@app.route('/criar-musica',methods=['POST'])
def criar_Musica():
    musica=request.get_json()
    firebase.criar(musica)
    return jsonify(musica)

@app.route('/musica',methods=['GET'])
def get_Musicas():
    musicas=firebase.get_musicas()
    return jsonify(musicas)

# @app.route('/musicas-hariel',methods=['GET'])
# def get_MusicasHariel():
#     musicas=firebase.get_musicas()
#     print('type',type(musicas))
#     print('musicas',musicas)
#     musicasHariel=[]
#     for musica in musicas:
#      print('musica',musicas[musica]['cantor'])
#     #  if musicas[musica]['cantor']=='MC Hariel':
#      if musicas[musica]['cantor']=='Matuê':
#         musicasHariel.append( musicas[musica])
#         # if (musicas[musica]=='MC Hariel'):
#         #     musicasHariel.append(musica)
#     return jsonify(musicasHariel)

app.run(port=5000,host='localhost',debug=True)