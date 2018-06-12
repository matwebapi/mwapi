from data_source_departament import DataSourceDepartament
from data_source_subject import DataSourceSubject
from data_sink_subject import DataSinkSubject
from data_sink_departament import DataSinkDepartament
from models import Subject,Departament

FGA = 0
FCE = 1
FUP = 2
DARCY = 3

departament = DataSourceDepartament.read("https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=4",FGA)
DataSinkDepartament.write(departament,FGA)
departament = DataSourceDepartament.read("https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=3",FCE)
DataSinkDepartament.write(departament,FCE)
departament = DataSourceDepartament.read("https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=2",FUP)
DataSinkDepartament.write(departament,FUP)
departament = DataSourceDepartament.read("https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=1",DARCY)
DataSinkDepartament.write(departament,DARCY)

subject = DataSourceSubject.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=650",FGA)
DataSinkSubject.write(subject)
subject = DataSourceSubject.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=660",FCE)
DataSinkSubject.write(subject)

"""

departament = Departament()
departament = DataSourceDepartamentGama.read(self=None)
DataSinkDepartamentGama.write(departament)

subject = Subject ()
subject = DataSourceSubjectFGA.read(self=None)
DataSinkSubjectFGA.write(subject)

departament = Departament()
departament = DataSourceDepartamentCeilandia.read(self=None)
DataSinkDepartamentCeilandia.write(departament)

departament = Departament()
departament = DataSourceSubjectFCE.read(self=None)
DataSinkSubjectFCE.write(departament)

departament = Departament()
departament = DataSourceDepartamentPlanaltina.read(self=None)
DataSinkDepartamentPlanaltina.write(departament)

departament = Departament()
departament = DataSourceDepartamentDarcy.read(self=None)
DataSinkDepartamentDarcy.write(departament)

departament = Departament()
departament = DataSourceSubjectFUP.read(self=None)
DataSinkSubjectFUP.write(departament)

departament = Departament()
departament = DataSourceSubjectDarcyCDT.read(self=None)
DataSinkSubjectDarcyCDT.write(departament)
"""