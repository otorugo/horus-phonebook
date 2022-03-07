from pydantic import BaseModel
from abc import ABC, abstractmethod


class BaseDTO(BaseModel, ABC):
    def inputDTO(self):
        return self.dict()

    @abstractmethod
    def outputDTO(self):
        pass

    def _outputDTO(self, removable_keys: list):
        output_dict = self.dict().copy()
        for key in removable_keys:
            del output_dict[key]
        return output_dict
