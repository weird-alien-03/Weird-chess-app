
# tests/conftest.py
import pytest

from app.repo import connect, create_schema

@pytest.fixture
def db_path(tmp_path):
    path = tmp_path / "test.db"
    with connect(path) as conn:
        create_schema(conn)
    return path
