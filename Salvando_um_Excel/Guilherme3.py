from distutils import dep_util
import requests
import pandas as pd
from datetime import datetime
from pytz import timezone
from bs4 import BeautifulSoup
links= []
i=-1
def get_links(URL,Depth,filename):
    global i
    i=i+1
    pagina = requests.get(URL)
    soup = BeautifulSoup(pagina.content,'html.parser')
    Div_a = soup.find_all('a',class_='')
    Div_b = []

    horario=[]
    data_e_hora_atuais = datetime.now()
    fuso_horario = timezone('Brazil/East')
    data_e_hora = data_e_hora_atuais.astimezone(fuso_horario)
    data_e_hora = data_e_hora.strftime('%d/%m/%Y %H:%M')

    for b in Div_a:
        if b.has_attr('href'):
            Div_b.append(b['href'])
    for a in Div_b:
        if 'https' in a:
            links.append(a)
            horario.append(data_e_hora)
    print(i)
    print(len(set(links)))
    print(links[i])
    if Depth == 0:
        pass
    '''else:                                      NÃO CONSEGUI FAZER O PROGRAMA RODAR COM O DEPTH DIFERENTE DE 0, POIS
        while i != 21:                            EU PRECISO RESTRINGIR O NUMERO DE VEZES QUE ELE RODA PARA SER = AO TAMANHO
            get_links(links[i],Depth,filename)    DA LISTA DE LINKS DA PRIMEIRA RODADA, SE O DEPTH FOR 2 COM O TAMANHO DA LISTA NA 2 RODADA E ASSIM EM DIANTE'''
    dados = pd.DataFrame(zip(set(links),horario),
                            columns=['LINKS','HORARIO'])
    dados.to_excel(filename)
    
get_links('https://github.com/GuilhermeFusari?tab=repositories',0,'tabela.xls')


