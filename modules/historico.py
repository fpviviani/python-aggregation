class Historico():

    def __init__(self, aluno):
        self.__aluno = aluno
        self.__disciplinas = []

    def getDisciplinas(self):
        return self.__disciplinas

    def addDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)


    
