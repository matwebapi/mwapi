import requests
from bs4 import BeautifulSoup
from models import Departament

url_gama = "https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=650"

departament_gama = Departament()

request = requests.get(url_gama)
soup = BeautifulSoup(request.text, "lxml")

list = soup.find_all("table", class_="table table-striped table-bordered")
cont = 0

for lista_td in list:

    lista = lista_td.find_all("tr")
    for lista_dados in lista:
        if lista_dados.next_element.name == "td":
            print(lista_dados.next_element.text)
