from pipers import Pipers
import json

class DataSinkSubjectFGA(Pipers):

    def write(subjects):

        data = {
            "DISCIPLINAS": {
                "CODIGO": subjects.list_cods,
                "MATERIA": subjects.list_names
            }
        }

        with open("disciplinas_fga.json", "w") as write_file:
            json.dump(data, write_file)

class DataSinkDepartamentGama(Pipers):

    def write(departament):

        data = {
            "DEPARTAMENTOS_GAMA": {
                "CODIGO": departament.cod,
                "SIGLA": departament.initials,
                "DENOMINACAO": departament.name
            }
        }

        with open("departamentos_gama.json", "w") as write_file:
            json.dump(data, write_file)

class DataSinkDepartamentCeilandia(Pipers):

    def write(departament):

        data = {
            "DEPARTAMENTOS_CEILANDIA": {
                "CODIGO": departament.cod,
                "SIGLA": departament.initials,
                "DENOMINACAO": departament.name
            }
        }

        with open("departamentos_ceilandia.json", "w") as write_file:
            json.dump(data, write_file)

class DataSinkDepartamentPlanaltina(Pipers):

    def write(departament):

        data = {
            "DEPARTAMENTOS_PLANALTINA": {
                "CODIGO": departament.cod,
                "SIGLA": departament.initials,
                "DENOMINACAO": departament.name
            }
        }

        with open("departamentos_planaltina.json", "w") as write_file:
            json.dump(data, write_file)

class DataSinkDepartamentDarcy(Pipers):

    def write(departament):

        data = {
            "DEPARTAMENTOS_DARCY_RIBEIRO": {
                "CODIGO": departament.list_cods,
                "SIGLA": departament.list_initials,
                "DENOMINACAO": departament.list_names
            }
        }

        with open("departamentos_darcy.json", "w") as write_file:
            json.dump(data, write_file)