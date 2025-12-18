
# tests/test_repo_tournaments.py
from app.repo import connect, create_tournament

def test_create_tournament_returns_id(db_path):
    with connect(db_path) as conn:
        tid1 = create_tournament(conn,"Alice", 1)
        tid2 = create_tournament(conn,"Bob", 2)
    assert tid1 != tid2
