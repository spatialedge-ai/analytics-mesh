from abc import ABCMeta
import logging
log = logging.getLogger(__name__)
import sys
import os

# add the library path - this should likely be in a env.py
#sys.path.append(os.path.dirname(__file__))


class Connection(metaclass=ABCMeta):
    """
    A connection base for connections to datasources or other services
    """
    def __init__(self, *args, **kwargs):
        pass


class Data(metaclass=ABCMeta):

    def __init__(self):
        self.data = None

    def read(self, *args, **kwargs):
        """
        read data
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def to_panda(self, *args, **kwargs):
        pass

    def write(self, *args, **kwargs):
        """
        write data
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def __iter__(self):
        """
        iterator of the data object
        :return:
        """
        pass


class FrameOperator(metaclass=ABCMeta):
    """
    frame operator class that operates on a dataframe
    """
    pass


class Count(FrameOperator):

    def __init__(self, pd_frame):
        super(Count, self).__init__()
        self.df = pd_frame

    def do(self):
        return len(self.df.index)
