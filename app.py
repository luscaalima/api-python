from flask import Flask, jsonify, request
from flask_cors import CORS
from app_firebase import *
app=Flask(__name__)
CORS(app)

link='https://lucas-firebase-default-rtdb.firebaseio.com'

firebase = Firebase(link)


@app.route('/criar-musica',methods=['POST'])
def criar_Musica():
    musica=request.get_json()
    print('criar-musica',musica)
    firebase.criar(musica)
    return jsonify(musica)

@app.route('/musica',methods=['GET'])
def get_Musicas():
    musicas=firebase.get_musicas()
    all_musicas =[]
    for music in musicas:
        print(musicas[music])
        all_musicas.append(musicas[music])
    return jsonify(all_musicas)



@app.route('/editar-musica',methods=['PATCH'])
def edit_Musicas():
    musicas=firebase.get_musicas()
    musicaEdit=request.get_json()
    # print('Musica antiga usar para pegar id',musicaEdit[0])
    # print('Musica nova',musicaEdit[1])
    all_musicas =[]
    for music in musicas:
        # print(musicas[music]['nome'])
        # print(musicas[music]['cantor'])
        if musicas[music]['nome']==musicaEdit[0]['nome'] and  musicas[music]['cantor']==musicaEdit[0]['cantor'] :
        #  print('id',music)
         firebase.editar_musica(music,musicaEdit[1]) 
         break
       
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
#         #     musicasHariel.append(usica)
#     return jsonify(musicasHariel)m

app.run(port=5000,host='localhost',debug=True)