
# tests/test_repo_players.py
from app.repo import connect, insert_player

def test_insert_player_returns_id(db_path):
    with connect(db_path) as conn:
        pid1 = insert_player(conn, "Alice")
        pid2 = insert_player(conn, "Bob")
    assert pid1 != pid2
