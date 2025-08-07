import tempfile
from datetime import datetime, UTC
from database_infra.sqlite_repo import SQLiteRepo
from logs.request_entry import RequestEntry


def test_save_and_list():
    db_path = tempfile.NamedTemporaryFile().name
    repo = SQLiteRepo(db_path=db_path)

    entry = RequestEntry(
        op_type="pow",
        input_args=[2, 3],
        result=8,
        timestamp=datetime.now(UTC),
    )

    saved = repo.save(entry)

    results = repo.list()
    assert len(results) == 1
    assert results[0].id == saved.id
    assert results[0].result == saved.result
    assert results[0].op_type == saved.op_type
