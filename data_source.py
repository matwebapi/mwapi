import requests
from bs4 import BeautifulSoup
from models import Subject,Departament
from pipers import Pipers
from filters import FilterSubjects

class DataSourceSubjectFGA(Pipers):

    def read(self):

        subject = Subject()
        filter_subjects = FilterSubjects

        url_subjects = "https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=650"
        request = requests.get(url_subjects)
        soup = BeautifulSoup(request.content, "html.parser")
        list_all_codes = soup.find_all("table", class_="table table-striped table-bordered")

        list_subjects = []

        for tr in soup.find_all('tr'):

            for td in tr.find_all('td'):
                list_subjects.append(td.text)

        for list_td in list_all_codes:

            list = list_td.find_all("tr")
            for list_data in list:

                if list_data.next_element.name == "td":
                    subject.list_cods.append(list_data.next_element.text)

        list_subjects = filter_subjects.blank_space(list_subjects)
        list_subjects = filter_subjects.remove_word_event_note(list_subjects)
        list_subjects = filter_subjects.remove_hours(list_subjects)
        subject.list_codes = filter_subjects.remove_vogals(list_subjects)
        subject.list_names = filter_subjects.remove_cod_of_list_name(subject.list_codes, list_subjects)
        subject.list_names = filter_subjects.remove_accents(subject.list_names)
        subject.list_names = filter_subjects.upper_words(subject.list_names)

        return subject

class DataSourceDepartamentGama(Pipers):

    def read(self):

        departament = Departament()
        url_departament_gama = "https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=4"

        request = requests.get(url_departament_gama)
        soup = BeautifulSoup(request.content, "html.parser")
        filter_subjects = FilterSubjects

        list_content = []
        for tr in soup.find_all('tr'):

            for td in tr.find_all('td'):
                list_content.append(td.text)

        list_content = filter_subjects.blank_space(list_content)
        list_content = filter_subjects.remove_accents(list_content)

        departament.cod = list_content[0]
        departament.name = list_content[2]
        departament.initials = list_content[1]

        departament.initials.upper()
        departament.name.upper()

        return departament

class DataSourceDepartamentCeilandia(Pipers):

    def read(self):

        departament = Departament()
        url_departament_ceilandia = "https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=3"

        request = requests.get(url_departament_ceilandia)
        soup = BeautifulSoup(request.content, "html.parser")
        filter_subjects = FilterSubjects

        list_content = []
        for tr in soup.find_all('tr'):

            for td in tr.find_all('td'):
                list_content.append(td.text)

        list_content = filter_subjects.blank_space(list_content)
        list_content = filter_subjects.remove_accents(list_content)

        departament.cod = list_content[0]
        departament.name = list_content[2]
        departament.initials = list_content[1]

        departament.name.upper()
        departament.initials.upper()

        return departament

class DataSourceDepartamentPlanaltina(Pipers):

    def read(self):

        departament = Departament()
        url_departament_planaltina = "https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=2"

        request = requests.get(url_departament_planaltina)
        soup = BeautifulSoup(request.content, "html.parser")
        filter_subjects = FilterSubjects

        list_content = []
        for tr in soup.find_all('tr'):

            for td in tr.find_all('td'):
                list_content.append(td.text)

        list_content = filter_subjects.blank_space(list_content)
        list_content = filter_subjects.remove_accents(list_content)

        departament.cod = list_content[0]
        departament.name = list_content[2]
        departament.initials = list_content[1]

        departament.initials.upper()
        departament.name.upper()

        return departament

class DataSourceDepartamentDarcy(Pipers):

    def read(self):

        departament = Departament()
        url_departament_darcy = "https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=1"

        request = requests.get(url_departament_darcy)
        soup = BeautifulSoup(request.content, "html.parser")
        filter_subjects = FilterSubjects

        list_content = []
        list_names = []
        list_cods = []
        list_initials = []

        for tr in soup.find_all('tr'):

            for td in tr.find_all('td'):
                list_content.append(td.text)

        list_content = filter_subjects.blank_space(list_content)
        list_content = filter_subjects.upper_words(list_content)
        list_cods = filter_subjects.remove_vogals(list_content)
        list_cods = filter_subjects.remove_initials(list_cods)
        list_initials = filter_subjects.remove_cod_of_list_name(list_cods,list_content)
        list_names = filter_subjects.search_names(list_initials)
        list_initials = filter_subjects.search_initials(list_initials)

        departament.list_cods = list_cods
        departament.list_initials = list_initials
        departament.list_names = filter_subjects.remove_accents(list_names)

        return departament