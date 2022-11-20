from flask import Flask, jsonify, request
from flask_cors import CORS
from app_firebase import *
from spotify import *



app=Flask(__name__)
CORS(app)

link='https://lucas-firebase-default-rtdb.firebaseio.com'
uri ="21xvcn6zyzksfnnnupym6r2ha"

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
    
    playlists=sp.get_playlists()['items']
    for playlist in  playlists:
        print('->',playlist,'\n')
    # print('playlists - >',playlists) 
    return jsonify(playlists)  

# @app.route('/sp-get-devices',methods=['GET'])
# def get_devices():
#     scope='user-read-playback-state'
#     sp = Spotify(scope)
#     return jsonify(sp.get_devices()) 

@app.route('/sp-get-playlists-musics',methods=['GET'])
def get_musicas_playlist():
    scope='user-modify-playback-state'
    sp = Spotify(scope)
    musicas_playlist=sp.get_musicas_playlist('7arOXPDBqETizFMQmAD1zB')
    print(musicas_playlist)
    # print(sp.get_playlists()) 
    # return jsonify(sp.get_playlists()) 
    return jsonify(musicas_playlist)


@app.route('/sp-next-music',methods=['GET'])
def next_music():
    device_id=get_device_id()
    # print(device_id)
    scope='user-modify-playback-state'
    sp = Spotify(scope)
    sp.next_music(device_id)
    return jsonify("PROXIMA")


@app.route('/sp-create-playlist',methods=['POST'])
def create_playlist():
    user_id =get_me()
    scope = "playlist-modify-public"
    sp = Spotify(scope)
    sp.create_playlist(user_id,"nome da playlist")
    return jsonify("PROXIMA")


@app.route('/sp-add-music-playlist',methods=['POST'])
def add_music_playlist():
    scope = "playlist-modify-public"
    sp = Spotify(scope)
    items=["spotify:track:3ZtHHGpAPSWC7Gnios4lmK","spotify:track:1iaPDgTbsKrlznVu13EWIf"]
    sp.add_music_playlist("7arOXPDBqETizFMQmAD1zB",items)
    return jsonify("PROXIMA")



@app.route('/sp-add-next-music',methods=['POST'])
def add_next_music():
    uri =request.get_json()['uri']
    scope='user-modify-playback-state'
    sp = Spotify(scope)
    sp.add_next_music(uri)
    return jsonify("ADD")

@app.route('/sp-music-now',methods=['GET'])
def music_now():
    idMusica='7HjZD0NPC1hzFpjUjo45GR'
    scope='user-read-playback-state'
    sp = Spotify(scope)
    sp.music_now()
    return jsonify(sp.music_now())

@app.route('/sp-brabos',methods=['GET'])
def brabos():
    scope='user-top-read'
    sp = Spotify(scope)
    sp.brabos()
    return jsonify(sp.brabos()['items'])


@app.route('/sp-add-music-likes',methods=['POST'])
def add_music_likes():
    scope='user-library-modify'
    sp = Spotify(scope)
    track_body = request.get_json()
    track=track_body['uri']
    sp.add_music_likes(track)
    return jsonify(sp.add_music_likes(track))


@app.route('/sp-del-music-likes',methods=['PUT'])
def del_music_likes():
    scope='user-library-modify'
    sp = Spotify(scope)
    track_body = request.get_json()
    track=track_body['uri']
    sp.del_music_likes(track)
    return jsonify(sp.del_music_likes(track))


#GETTERS
def get_device_id(): 
    scope='user-read-playback-state'
    sp = Spotify(scope)
    return sp.get_devices()['devices'][0]['id']

def get_me(): 
    scope='user-read-private'
    sp = Spotify(scope)
    # print(sp.get_me()['id'])
    return sp.get_me()['id']
 


app.run(port=5000,host='localhost',debug=True)