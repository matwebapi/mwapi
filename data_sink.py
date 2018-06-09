from pipers import Pipers

class Data_Sink(Pipers):

    """

    data = {
        "subjects": {
            "CODIGO": subjects.list_cods,
            "MATERIA": subjects.list_names
        }
    }

    "Gera JSON"
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file)
    """
