from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def validate(self, data: dict) -> Exception:
        pass
