from abc import ABCMeta, abstractmethod

class Pipers(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self):

        pass

    @abstractmethod
    def write(self):

        pass