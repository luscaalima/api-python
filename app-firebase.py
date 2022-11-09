import requests
import json

link='https://lucas-firebase-default-rtdb.firebaseio.com'

dados={
    'cliente':'Pipico',
    'preco':'500',
    'produto':'Celular',
}


requisicao = requests.post(f'{link}/Vendas/.json',data=json.dumps(dados))
print(requisicao)
print(requisicao.text)