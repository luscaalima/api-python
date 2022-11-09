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
        
    def criar_Categoria(self,categoria,item):   
       print(item)    
       
       requisicao = requests.post(f'{self.url}/{categoria}/.json',data=json.dumps("item"))
       print(requisicao)
    #    print(requisicao.status)
       print(requisicao.text)
     