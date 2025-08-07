from .operation_base import OperationBase


class PowerOperation(OperationBase):
    def execute(self, a, b):
        if not isinstance(a, int) or not isinstance(b, int):
            raise TypeError("a and b must be integers")
        return a ** b
