
#tests/test_fetch_game.py

import app.repo as repo
from app.models import Game

def test_fetch_game(db_path):
    with repo.connect(db_path) as conn:
        tid = repo.create_tournament(conn, "1st tournament", 4)
        rid = repo.create_round(conn, tid, 1)
        p1 = repo.insert_player(conn, "Hikaru")
        p2 = repo.insert_player(conn, "Vishy")
        p3 = repo.insert_player(conn, "Gukesh")
        gid1 = repo.insert_game(conn, rid, p1, p2)
        gid2 = repo.insert_game(conn, rid, p3, p1)
        repo.update_game_result(conn, gid1, "1-0")
        repo.update_game_result(conn, gid2, "1/2-1/2")
        games = repo.fetch_games_for_tournament(conn,tid)
    assert len(games)==2
