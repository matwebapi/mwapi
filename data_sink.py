from pipers import Pipers
import json

class DataSinkDepartamentGama(Pipers):

    def write(departament):

        data = {
            "DEPARTAMENTOS_GAMA": {
                "CODIGO": departament.cod,
                "SIGLA": departament.initials,
                "DENOMINACAO": departament.name
            }
        }

        with open("DEPARTAMENTOS_GAMA.json", "w") as write_file:
            json.dump(data, write_file)

class DataSinkSubjectFGA(Pipers):

    def write(subjects):

        data = {
            "DISCIPLINAS_FGA": {
                "CODIGO": subjects.list_cods,
                "MATERIA": subjects.list_names
            }
        }

        with open("DISCIPLINAS_FGA.json", "w") as write_file:
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

        with open("DEPARTAMENTOS_CEILANDIA.json", "w") as write_file:
            json.dump(data, write_file)

class DataSinkSubjectFCE(Pipers):

    def write(subjects):

        data = {
            "DISCIPLINAS_FCE": {
                "CODIGO": subjects.list_cods,
                "MATERIA": subjects.list_names
            }
        }

        with open("DISCIPLINAS_FCE.json", "w") as write_file:
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

        with open("DEPARTAMENTOS_PLANALTINA.json", "w") as write_file:
            json.dump(data, write_file)

class DataSinkSubjectFUP(Pipers):

    def write(subjects):

        data = {
            "DISCIPLINAS_FCE": {
                "CODIGO": subjects.list_cods,
                "MATERIA": subjects.list_names
            }
        }

        with open("DISCIPLINAS_FUP.json", "w") as write_file:
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

        with open("DEPARTAMENTOS_DARCY.json", "w") as write_file:
            json.dump(data, write_file)