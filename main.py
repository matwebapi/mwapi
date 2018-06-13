from data_source_departament import DataSourceDepartament
from data_source_subject import DataSourceSubject,DataSourceSubjectsDarcy
from data_sink_subject import DataSinkSubject
from data_sink_departament import DataSinkDepartament

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

subject = DataSourceSubject.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=638",FUP)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=383","CDS",383)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=025","CEAM",25)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=039","CET",39)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=135","DEG",3)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=004","DEX",4)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=402","ADM",402)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=135","DAN",135)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=422","CEM",422)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=421","VIS",421)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=432","DAP",432)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=121","CEL",121)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=129","BOT",129)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=116","CIC",116)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=125","CFS",125)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=424","DIN",424)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=127","ECL",127)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=405","ECO",405)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=177","ENF",177)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=162","ENC",162)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=725","EPR",725)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=163","ENE",163)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=165","EFL",165)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=164","ENM",164)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=115","EST",115)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=352","ELA",352)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=137","FIL",137)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=128","FIT",128)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=126","GEN",126)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=138","GEA",138)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=406","GPP",406)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=139","HIS",139)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=431","JOR",431)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=149","LET",149)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=147","LIP",147)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=113","MAT",113)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=192","MTC",193)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=423","MUS",423)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=176","NUT",176)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=178","ODT",178)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=194","PAD",194)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=411","PPB",441)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=157","PRO",157)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=412","PED",412)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=413","PCL",413)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=414","PST",414)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=179","DSC",179)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=136","SER",136)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=134","SOL",134)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=158","TEC",158)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=191","TEF",191)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=148","TEL",148)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=382","ZOO",382)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=404","CCA",404)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=159","THAU",159)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=120","IBD",120)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=410","IPE",410)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=40","FACE",40)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=540","FAV",540)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=700","FCI",700)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=17","FS",17)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=430","FAC",430)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=500","FDD",500)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=19","FE",19)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=530","FEF",530)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=570","FMD",570)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=16","FT",16)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=420","IDA",420)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=508","IPOL",508)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=12","ID",12)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=13","IH",13)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=550","IFD",550)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=440","IGD",440)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=14","IL",14)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=560","IQD",560)
DataSinkSubject.write(subject)

subject = DataSourceSubjectsDarcy.read("https://matriculaweb.unb.br/graduacao/oferta_dis.aspx?cod=589","IREL",589)
DataSinkSubject.write(subject)