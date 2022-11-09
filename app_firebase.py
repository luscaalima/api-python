import requests
import json

# link='https://lucas-firebase-default-rtdb.firebaseio.com'

# dados={
#     'cliente':'Outro Pipico',
#     'preco':'900',
#     'produto':'Telefone',
# }






class Firebase:
    def __init__(self,url): 
        self.url = url
    
    # INCLUIR MUSICA POST)    
    def criar(self,musica):    
        print(musica)
        musyc = {'nome': 'nome-musica', 'cantor': 'nome-cantor'}
        requisicao = requests.post(f'{self.url}/musica/.json', data=json.dumps(musica))
        print(requisicao)
        print(requisicao.text) 
           
    def get_musicas(self):
        requisicao = requests.get(f'{self.url}/musica/.json')
        # print('requisicao',requisicao)
        # print('requisicao.text',type(requisicao.text)) 
        # print('type',type(json.loads(requisicao.text))) 
        return json.loads(requisicao.text)
    
     