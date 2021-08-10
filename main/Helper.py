from abc import ABC, abstractmethod

class Helper(ABC):

    @abstractmethod
    def convert_to_heading(self):
        pass

    @abstractmethod
    def convert_to_notes(self):
        pass

    @abstractmethod
    def convert_to_item(self):
        pass