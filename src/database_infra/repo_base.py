from abc import ABC, abstractmethod


class RepoBase(ABC):
    @abstractmethod
    def save(self, log):
        raise NotImplementedError

    @abstractmethod
    def list(self):
        raise NotImplementedError
