import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
client_id="fbb9a866ad494ad4a92e468687de78b4"
client_secret="af094ee8f9224eaf9aa5c7c5b5bb8043"
    
auth_manager = SpotifyClientCredentials(client_id,client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)
# print(sp.current_user())
# find album by name
album = "Maquina do Tempo"
results = sp.search(q = "album:" + album, type = "album")
print('results',results)
print('results',results['albums']['items'][0]['artists'][0]['external_urls']['spotify'])
# print('results',results['albums'][0])
# get the first album uri
# album_id = results['albums']['items'][0]['uri']
# print(sp.current_user_follow_playlist())
# playlists = sp.user_playlists('spotify',5)
# print('playlists',playlists)
# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None    


