
# tests/test_constraints.py

import sqlite3
import pytest
from app.repo import connect, create_tournament, create_round

#to check that it rejects zero round

def test_tournament_constraint(db_path):
    with connect(db_path) as conn:
        with pytest.raises(sqlite3.IntegrityError):
            create_tournament(conn,"Bad",0)

def test_round_constraint(db_path):
    with connect(db_path) as conn:
        tid = create_tournament(conn, "Tbad", 4)
        create_round(conn, tid, 1)
        with pytest.raises(sqlite3.IntegrityError):
            create_round(conn, tid, 1)
