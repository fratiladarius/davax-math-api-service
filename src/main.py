from logs.request_entry import RequestEntry
from math_operations.operations_factory import OperationFactory
from database_infra.repo_factory import RepositoryFactory

repo = RepositoryFactory().build()

operation_name = 'fact'
input_args = [3]

operation_factory = OperationFactory()
operation = operation_factory.get(operation_name)

result = operation.execute(*input_args)

log_entry = RequestEntry(
    op_type=operation_name,
    input_args=input_args,
    result=result,
)

repo.save(log_entry)

for entry in repo.list():
    print(
        f'operation type: {entry.op_type}\n'
        f'input args: {entry.input_args}\n'
        f'result: {entry.result}\n'
        f'timestamp: {entry.timestamp}',
    )
