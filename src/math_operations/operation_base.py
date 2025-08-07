from abc import ABC, abstractmethod


class OperationBase(ABC):
    @abstractmethod
    def execute(self, *args):
        raise NotImplementedError
