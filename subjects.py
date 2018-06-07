import requests
from bs4 import BeautifulSoup
from models import Subjects
import json

subjects = Subjects()

url_subjects = "https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=650"
request = requests.get(url_subjects)
soup = BeautifulSoup(request.content, "html.parser")
list_all = soup.find_all("table", class_="table table-striped table-bordered")

list = []
list_names = []
list_codes = []
list_codes_cod = []

"""
Processo para retirar as informações da tabela de lista de matérias,via requesição.
"""

for row in soup.find_all('tr'):
    for cell in row.find_all('td'):
        list.append(cell.text)

"""
Tira espaços em branco da lista
"""

while '' in list :
    list.remove('')

"""
Tira a palavra 'event_note' da lista
"""
while 'event_note' in list:
    list.remove('event_note')
"""
Filtragem dos dados
"""

list = [x for x in list if "h" not in x]

list_codes = [x for x in list if "A" not in x]
list_codes = [x for x in list if "O" not in x]

list_names = [x for x in list if not any(ignore in x for ignore in list_codes)]

for lista_td in list_all:

    lista = lista_td.find_all("tr")
    for lista_dados in lista:
        if lista_dados.next_element.name == "td":
            list_codes_cod.append(lista_dados.next_element.text)

for aux in range(len((list_codes_cod))):
    subjects.list_cods = list_codes_cod

for aux in range(len(list_names)):
    subjects.list_names = list_names

"""
Tirando acentuação das palavras
"""

subjects.list_names = [x.replace('Á','A') for x in subjects.list_names]
subjects.list_names = [x.replace('À','A') for x in subjects.list_names]
subjects.list_names = [x.replace('Â','A') for x in subjects.list_names]
subjects.list_names = [x.replace('Ã','A') for x in subjects.list_names]
subjects.list_names = [x.replace('É','E') for x in subjects.list_names]
subjects.list_names = [x.replace('Ê','E') for x in subjects.list_names]
subjects.list_names = [x.replace('Í','I') for x in subjects.list_names]
subjects.list_names = [x.replace('Õ','O') for x in subjects.list_names]
subjects.list_names = [x.replace('Ô','O') for x in subjects.list_names]
subjects.list_names = [x.replace('Ó','O') for x in subjects.list_names]
subjects.list_names = [x.replace('Ç','C') for x in subjects.list_names]

"""
Formatação para o JSON
"""
data = {
    "subjects": {
        "CODIGO" : subjects.list_cods,
        "MATERIA" : subjects.list_names
    }
}

"Gera JSON"
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)