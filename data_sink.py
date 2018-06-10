from pipers import Pipers
import json

class DataSinkSubject(Pipers):

    def write(subjects):

        data = {
            "subjects": {
                "CODIGO": subjects.list_cods,
                "MATERIA": subjects.list_names
            }
        }

        with open("disciplinas_fga.json", "w") as write_file:
            json.dump(data, write_file)