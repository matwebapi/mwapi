import requests
from bs4 import BeautifulSoup
from models import Subject
from pipers import Pipers
from filters import FilterSubjects

class DataSourceSubject(Pipers):

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