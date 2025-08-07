from pathlib import Path
from .sqlite_repo import SQLiteRepo


class RepositoryFactory:
    _map = {
        'sqlite': lambda path: SQLiteRepo(path),
    }

    def build(self, backend: str = 'sqlite'):
        if backend not in self._map:
            raise ValueError(f'unknown repo backend {backend!r}')

        if backend == 'sqlite':
            db_path = Path(__file__).parent / 'dbs' / 'sqlite_database.db'
            db_path.parent.mkdir(parents=True, exist_ok=True)
            return self._map[backend](db_path)
