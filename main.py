from modules import curso as c
from modules import disciplina as d
from modules import aluno as a

sin = c.Curso("Sistemas")
bli = c.Curso("Biologia")
com220 = d.Disciplina("COM220", "POO", 72, sin.getGrade())
com240 = d.Disciplina("COM240", "Redes", 68, sin.getGrade())
sin210 = d.Disciplina("SIN210", "Governança", 48, sin.getGrade())
bio132 = d.Disciplina("BIO132", "Biologia da Conservação", 72, bli.getGrade())
bio230 = d.Disciplina("BIO230", "Anatomia", 35, bli.getGrade())
lic421 = d.Disciplina("LIC421", "Prática de Ensino", 89, bli.getGrade())

fabio = a.Aluno(2017006774, "Fábio", sin)
historicoFabio = fabio.getHistorico()
historicoFabio.addDisciplina(com220)
historicoFabio.addDisciplina(bio230)
historicoFabio.addDisciplina(sin210)
historicoFabio.addDisciplina(bio132)

cargaObrigatoria = 0
cargaEletiva = 0

for disciplina in historicoFabio.getDisciplinas():
    if (disciplina.getGrade().getCurso() == fabio.getCurso()):
        cargaObrigatoria += disciplina.getCargaHoraria()
    else:
        cargaEletiva += disciplina.getCargaHoraria()

print("\nCarga horária total das disciplinas obrigatórias cursadas: {} horas".format(cargaObrigatoria))
print("Carga horária total das disciplinas eletivas cursadas: {} horas".format(cargaEletiva))
