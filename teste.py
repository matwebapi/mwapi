from data_source import DataSourceSubject
from data_sink import DataSinkSubject
from models import Subject

subject = DataSourceSubject.read(self=None)
DataSinkSubject.write(subject)

print("Testando o Estilo Arquitetural Papers And Filters")
