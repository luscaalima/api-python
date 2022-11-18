import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
import requests
import json
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
     
    def get_me(self):
     return self.sp.me()
                    
    def next_music(self,device_id):
     return self.sp.next_track(device_id)

    def create_playlist(self,user_id,nome_playlist):
      return self.sp.user_playlist_create(user_id,name=nome_playlist)
        
    def add_music_playlist(self,playlist_id,items):
      return  self.sp.playlist_add_items(playlist_id=playlist_id,items=items,position=1)

    def get_musicas_playlist(self,id):
      return  self.sp.playlist_items(id)
  
    def add_next_music(self,uri):
      return  self.sp.add_to_queue(uri)
    
    def music_now(self):
      return  self.sp.currently_playing()
    
    def brabos(self):
      return self.sp.current_user_top_tracks(limit=8)