from modules import grade as g

class Curso():

    def __init__(self, nome):
        self.__nome = nome
        self.__grade = g.Grade(2020, self)

    def getNome(self):
        return self.__nome

    def getGrade(self):
        return self.__grade