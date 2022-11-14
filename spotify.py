import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
client_id="fbb9a866ad494ad4a92e468687de78b4"
client_secret="af094ee8f9224eaf9aa5c7c5b5bb8043"
auth_manager = SpotifyClientCredentials(client_id,client_secret)
# print(auth_manager.get_access_token())
access_token= auth_manager.get_access_token()
# print('token',token['access_token'])
# access_token =token['access_token']
# print('token',access_token)


# BASE_URL = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
BASE_URL = 'https://api.spotify.com'
token=access_token['access_token']

headers = {'Authorization': "Bearer {}".format(token)}
auth_response = requests.get(f'{BASE_URL}/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V', headers=headers)
print(auth_response)

#Obter listas de reprodução do usuário atual
endpointListas = f'{BASE_URL}/v1/me/playlists'
print('endpoint',endpointListas)
listaReprodução = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
print(listaReprodução)