from data_source_departament import DataSourceDepartament
from data_source_subject import DataSourceSubject,DataSourceSubjectsDarcy
from data_sink_subject import DataSinkSubject
from data_sink_departament import DataSinkDepartament

DARCY = "DARCY"
FUP = "FUP"
FCE = "FCE"
FGA = "FGA"

cont = 0

list_departaments = [FGA,FCE,FUP,DARCY]
list_departaments_numbers = [4,3,2,1]
list_departaments_cods = [650,660,638]

for aux in range(len(list_departaments)):

    departament = DataSourceDepartament.read("https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=" +
                                             str(list_departaments_numbers[aux]), list_departaments[aux])
    DataSinkDepartament.write(departament, list_departaments[aux])

    for new_aux in range(len(list_departaments_cods)):

        subjects = DataSourceSubject.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=" +
                                          str(list_departaments_cods[new_aux]),list_departaments[new_aux])
        DataSinkSubject.write(subjects)

subjects_darcy = DataSourceDepartament.read("https://matriculaweb.unb.br/graduacao/oferta_dep.aspx?cod=" +
                                            str(list_departaments_numbers[3]),list_departaments[3])

subjects_darcy_cods = subjects_darcy.list_cods
subjects_darcy_initials = subjects_darcy.list_initials
size_subjects_darcy = 75

for aux in range(size_subjects_darcy):

    subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=" +
                                           str(subjects_darcy_cods[aux]),
                                           subjects_darcy_initials[aux],
                                           subjects_darcy_cods[aux])
    DataSinkSubject.write(subject)