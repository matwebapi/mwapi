from pipers import Pipers
import json

class DataSinkDepartament(Pipers):

    def write(departament,type):

        if (type < 3):

            data = {
                "DEPARTAMENTOS_" + departament.initials: {
                    "CODIGO": departament.cod,
                    "SIGLA": departament.initials,
                    "DENOMINACAO": departament.name
                }
            }
        else:

            data = {
                "DEPARTAMENTOS_DARCY_RIBEIRO": {
                    "CODIGO": departament.list_cods,
                    "SIGLA": departament.list_initials,
                    "DENOMINACAO": departament.list_names
                }
            }

        with open("DEPARTAMENTOS_" + departament.initials +".json", "w") as write_file:
            json.dump(data, write_file)