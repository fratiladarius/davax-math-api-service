from .power_op import PowerOperation
from .factorial_op import FactorialOperation
from .fibonacci_op import FibonacciOperation


class OperationFactory:
    _registry = {
        'pow': PowerOperation(),
        'fact': FactorialOperation(),
        'fib': FibonacciOperation()
    }

    def get(self, operation_name):
        return self._registry[operation_name]
