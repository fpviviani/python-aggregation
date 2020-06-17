from modules import historico as h

class Aluno():

    def __init__(self, nroMatric, nome, curso):
        self.__nroMatric = nroMatric
        self.__nome = nome
        self.__historico = h.Historico(self)
        self.__curso = curso

    def getNome(self):
        return self.__nome

    def getNroMatric(self):
        return self.__nroMatric

    def getHistorico(self):
        return self.__historico

    def getCurso(self):
        return self.__curso