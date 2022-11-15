import base64
import requests

link = "https://accounts.spotify.com/api/token"

client_id="fbb9a866ad494ad4a92e468687de78b4"
client_secret="af094ee8f9224eaf9aa5c7c5b5bb8043"

client_creds=f"{client_id}:{client_secret}"

client_creds_b64=base64.b64encode(client_creds.encode())

method="POST"
token_data={"grant_type": "client_credentials"}
token_header={"Authorization": f"Basic {client_creds_b64.decode()}"}

r=requests.post(url=link,data=token_data,headers=token_header,)
print(r.json())
access_token = r.json()
token=access_token['access_token']
print(token)