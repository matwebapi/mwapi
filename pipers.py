from abc import ABCMeta, abstractmethod

class Pipers(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def read(url,type):

        pass

    @abstractmethod
    def write(object,type):

        pass