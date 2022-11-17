import requests
import json

# link='https://lucas-firebase-default-rtdb.firebaseio.com'
class Firebase:
    def __init__(self,url): 
        self.url = url
    
    # INCLUIR MUSICA POST FIREBASE    
    def criar(self,musica):    
        print(musica)
        requisicao = requests.post(f'{self.url}/musica/.json', data=json.dumps(musica))
        print(requisicao)
        print(requisicao.text) 
           
    def get_musicas(self):
        requisicao = requests.get(f'{self.url}/musica/.json')
        return json.loads(requisicao.text)
    
    def editar_musica(self,id,musica):
        print (id)
        requisicao = requests.patch(f'{self.url}/musica/{id}/.json',data=json.dumps(musica))
        # print(requisicao)
        # print(requisicao.text)
        return json.loads(requisicao.text)
    
     