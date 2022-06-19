import requests
import json
from bs4 import BeautifulSoup
def get_metas(URL):
    pagina = requests.get(URL)
    soup = BeautifulSoup(pagina.content,'html.parser')
    Metas = soup.find_all("meta")
    nomes = []
    conteudo = []
    for i in Metas:
        if i.has_attr('name'):
            nomes.append(i['name'])
            conteudo.append(i['content'])
            print("Nome:",i['name'],"---" ,"Conteúdo:",i['content'])
    nomes_json = json.dumps(nomes)
    conteudo_json = json.dumps(conteudo)
    lista_json = {'Nomes':[nomes_json], 'Conteúdo':[conteudo_json]}
    return lista_json

get_metas("https://github.com/GuilhermeFusari?tab=repositories")