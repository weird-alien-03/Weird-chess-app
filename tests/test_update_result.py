
#tests/test_update_result.py
from app.repo import connect, insert_player, create_tournament
from app.repo import create_round, insert_game, update_game_result

def test_update_result(db_path):
    with connect(db_path) as conn:
        tid = create_tournament(conn, "1st tournament", 4)
        rid = create_round(conn, tid, 1)
        p1 = insert_player(conn, "Hikaru")
        p2 = insert_player(conn, "Vishy")
        gid = insert_game(conn, rid, p1, p2)
        update_game_result(conn, gid, "0-1")
        sql = "SELECT result FROM games WHERE id = ?"
        row = conn.execute(sql, (gid,)).fetchone()
    assert row["result"] == "0-1"
