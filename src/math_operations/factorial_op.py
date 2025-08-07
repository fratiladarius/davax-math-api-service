from .operation_base import OperationBase


class FactorialOperation(OperationBase):
    def execute(self, n):
        if n < 0:
            raise ValueError('n must be >= 0')
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
