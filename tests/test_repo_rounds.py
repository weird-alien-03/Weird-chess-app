
#tests/test_repo_rounds.py
from app.repo import connect, create_tournament, create_round

def test_create_round(db_path):
    with connect(db_path) as conn:
        tid = create_tournament(conn, "Magnus", 4)
        rid1 = create_round(conn, tid, 1)
        rid2 = create_round(conn, tid, 2)
    assert rid1 != rid2
