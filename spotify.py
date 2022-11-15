import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import requests

# auth_manager = SpotifyClientCredentials(client_id,client_secret)

# scope='user-read-playback-state'

class Spotify:
    client_id="fbb9a866ad494ad4a92e468687de78b4"
    client_secret="af094ee8f9224eaf9aa5c7c5b5bb8043"
    def __init__(self,scope):
         self.scope = scope
         self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=self.client_id,
                                                client_secret=self.client_secret,
                                                redirect_uri="http://localhost:4200/home",
                                                scope=self.scope))
    
    
    
    def get_playlists(self):
     return self.sp.current_user_playlists()
            
        
    def get_devices(self):
     return self.sp.devices()
            
      
    def next_music(self,device_id):
     return self.sp.next_track(device_id)
        
   
    # scope='app-remote-control'
    
    # sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fbb9a866ad494ad4a92e468687de78b4",
    #                                             client_secret="af094ee8f9224eaf9aa5c7c5b5bb8043",
    #                                             redirect_uri="http://localhost:4200/home",
    #                                             scope=scope))

    # loggedUser=sp.current_user()
    # print('sp.current_user()',loggedUser)
    # print(sp.devices())

    # # print(auth_manager.get_access_token())
    # access_token= auth_manager.get_access_token()
    # # print('token',token['access_token'])
    # # access_token =token['access_token']
    # # print('token',access_token)


    # # BASE_URL = 'https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V'
    # BASE_URL = 'https://api.spotify.com'
    # token=access_token['access_token']

    # headers = {'Authorization': "Bearer {}".format('BQAWwQxnXqXHl_buHQQwKcCET2g4Eng1gouZZA9lfQBD3gmF-8dsOefX4C1VAXh1ljPQppytzJEHINwWU2nneQSJMCAksSaWHrxMX_Jd_0cA17_yJfqapi_X0B2HhBeB6VAUKzo3VZUGzsx0U5QlHalWKoQ4B3V9SrCbaIQ-YOBzf_9miwL6jY9yBwd5fIKlJnfrwrsnyjBNyZWY')}
    # print(headers)
    # auth_response = requests.get(f'{BASE_URL}/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V', headers=headers)
    # print(auth_response)

    # #Obter listas de reprodução do usuário atual
    # endpointListas = f'{BASE_URL}/v1/me/playlists'
    # print('endpoint',endpointListas)
    # listaReprodução = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers)
    # print(listaReprodução)