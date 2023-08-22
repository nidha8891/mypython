from abc import ABC,abstractmethod
class Ide(ABC):

    def debug(self):
        pass

class pycharm (Ide):

    def debug(self):
        print("pycharm debug method")

class Eclipse(Ide):

    def debug(self):
        print("pycharm debug method")

class Eclipse(Ide):


    def debug(self):
        print("eclipse debug")

pyc=pycharm()
pyc.debug()