# Abstract class

from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass 