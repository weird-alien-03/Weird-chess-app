
#tests/test_repo_game.py
from app.repo import connect, insert_player, create_tournament
from app.repo import create_round, insert_game

def test_insert_game(db_path):
    with connect(db_path) as conn:
        tid = create_tournament(conn, "1st tournament", 4)
        rid = create_round(conn, tid, 1)
        p1 = insert_player(conn, "Hikaru")
        p2 = insert_player(conn, "Vishy")
        gid = insert_game(conn, rid, p1, p2)
        sql = "SELECT result FROM games WHERE id = ?"
        row = conn.execute(sql, (gid,)).fetchone()
    assert row["result"] == "PENDING"
        
