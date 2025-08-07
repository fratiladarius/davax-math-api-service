import json
import sqlite3

from .repo_base import RepoBase
from logs.request_entry import RequestEntry


class SQLiteRepo(RepoBase):
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self._init_schema()

    def _init_schema(self):
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS requests (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                op_type TEXT,
                input_args TEXT,
                result TEXT,
                timestamp TEXT
            )
            """
        )
        self.conn.commit()

    def save(self, log: RequestEntry):
        cursor = self.conn.execute(
            """
            INSERT INTO requests (op_type, input_args, result, timestamp)
            VALUES (?, ?, ?, ?)
            """,
            (
                log.op_type,
                json.dumps(log.input_args),
                str(log.result),
                log.timestamp.isoformat(),
            ),
        )
        self.conn.commit()

        log.id = cursor.lastrowid
        return log

    def list(self):
        self.conn.row_factory = sqlite3.Row
        cursor = self.conn.execute("SELECT * FROM requests")
        rows = cursor.fetchall()

        return [
            RequestEntry(
                id=row['id'],
                op_type=row["op_type"],
                input_args=json.loads(row["input_args"]),
                result=row["result"],
                timestamp=row["timestamp"],
            )
            for row in rows
        ]

    def get(self, entry_id):
        self.conn.row_factory = sqlite3.Row
        row = self.conn.execute(
            "SELECT * FROM requests WHERE id = ?", (entry_id, )).fetchone()
        if not row:
            return None

        return RequestEntry(
            id=row['id'],
            op_type=row["op_type"],
            input_args=json.loads(row["input_args"]),
            result=row["result"],
            timestamp=row["timestamp"],
        )

    def delete(self, entry_id):
        cursor = self.conn.execute(
            "DELETE FROM requests WHERE id = ?", (entry_id, ))
        self.conn.commit()
        return cursor.rowcount > 0
