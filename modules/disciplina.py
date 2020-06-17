class Disciplina():

    def __init__(self, cod, nome, cargaHoraria, grade):
        self.__cod = cod
        self.__nome = nome
        self.__cargaHoraria = cargaHoraria
        grade.addDisciplina(self)
        self.__grade = grade

    def getCod(self):
        return self.__cod

    def getNome(self):
        return self.__nome

    def getCargaHoraria(self):
        return self.__cargaHoraria

    def getGrade(self):
        return self.__grade