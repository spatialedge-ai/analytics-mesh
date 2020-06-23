from abc import ABCMeta


class Connector(metaclass=ABCMeta):

    def __init__(self):
        pass

    def connect(self, **kwargs):
        raise NotImplementedError('override method in base class')

