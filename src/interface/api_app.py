from flask import Flask, request, jsonify
from pydantic import BaseModel, ValidationError
from math_operations.operations_factory import OperationFactory
from database_infra.repo_factory import RepositoryFactory
from logs.request_entry import RequestEntry


app = Flask(__name__)

repo = RepositoryFactory().build()
ops = OperationFactory()


class CalcIn(BaseModel):
    op: str
    args: list[int]


@app.route("/")
def hello():
    return "hello, world"


@app.route("/calc", methods=["POST"])
def calc():
    try:
        data = CalcIn.model_validate(request.get_json(force=True))
    except ValidationError as err:
        return jsonify(err.errors()), 400

    try:
        operation = ops.get(data.op)
    except ValueError:
        return {"error": f"unknown op {data.op}"}, 404

    result = operation.execute(*data.args)
    entry = RequestEntry(
        op_type=data.op,
        input_args=data.args,
        result=result,
    )
    repo.save(entry)
    return entry.model_dump(), 200


@app.get("/logs")
def logs():
    return [e.model_dump() for e in repo.list()], 200


@app.get("/logs/<int:entry_id>")
def get_log(entry_id):
    entry = repo.get(entry_id)
    if not entry:
        return {"error": "not found"}, 404
    return entry.model_dump(), 200


@app.delete("/logs/<int:entry_id>")
def delete_log(entry_id):
    entry = repo.delete(entry_id)
    if not entry:
        return {"error": "not found"}, 404
    return {"deleted": True}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
