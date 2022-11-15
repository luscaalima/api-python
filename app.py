from flask import Flask, jsonify, request
from flask_cors import CORS
from app_firebase import *
from spotify import *



app=Flask(__name__)
CORS(app)

link='https://lucas-firebase-default-rtdb.firebaseio.com'

firebase = Firebase(link)


@app.route('/criar-musica',methods=['POST'])
def criar_Musica():
    musica=request.get_json()
    # print('criar-musica',musica)
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



@app.route('/editar-musica',methods=['PUT'])
def edit_Musicas():
    musicas=firebase.get_musicas()
    musicaEdit=request.get_json()
    # all_musicas =[]
    for music in musicas:
        if musicas[music]['nome']==musicaEdit[0]['nome'] and  musicas[music]['cantor']==musicaEdit[0]['cantor'] :
         firebase.editar_musica(music,musicaEdit[1]) 
         break
       
    return jsonify(musicas)

@app.route('/sp-get-playlists',methods=['GET'])
def get_playlists():
    scope='user-read-playback-state'
    sp = Spotify(scope)
    print(sp.get_playlists()) 
    return jsonify(sp.get_playlists())  

@app.route('/sp-get-devices',methods=['GET'])
def get_devices():
    scope='user-read-playback-state'
    sp = Spotify(scope)
    # device_id=sp.get_devices()['devices'][0]['id']
    # print('device_id',device_id) 
    # print(sp.get_devices()) 
    
    return jsonify(sp.get_devices()) 
#GETTER 
def get_device_id(): 
    scope='user-read-playback-state'
    sp = Spotify(scope)
    return sp.get_devices()['devices'][0]['id']
 
@app.route('/sp-next-music',methods=['GET'])
def next_music():
    device_id=get_device_id()
    print(device_id)
    scope='user-modify-playback-state'
    sp = Spotify(scope)
    sp.next_music(device_id)
    # print(sp.get_playlists()) 
    # return jsonify(sp.get_playlists()) 
    return jsonify("PROXIMA")


app.run(port=5000,host='localhost',debug=True)