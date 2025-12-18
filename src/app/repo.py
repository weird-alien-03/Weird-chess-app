

# src/app/repo.py
from __future__ import annotations
import sqlite3
from pathlib import Path
from typing import Iterator
from contextlib import contextmanager
from .models import Game

@contextmanager
def connect(db_path: str | Path) -> Iterator[sqlite3.Connection]:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    # must be enabled per-connection
    
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def create_schema(conn: sqlite3.Connection) -> None:
    sql = (Path(__file__).resolve().parents[2] /
           "schema.sql").read_text(encoding="utf-8")
    conn.executescript(sql)
    conn.commit()

def insert_player(conn: sqlite3.Connection, name: str) -> int:
    sql = "INSERT INTO players (name) VALUES (?)"
    cur = conn.execute(sql, (name,))
    return cur.lastrowid

def create_tournament(conn: sqlite3.Connection, name: str,
                      rounds_planned: int) -> int:
    sql = "INSERT INTO tournaments (name, rounds_planned) VALUES (?,?)"
    cur = conn.execute(sql, (name, rounds_planned))
    return cur.lastrowid

def create_round(conn: sqlite3.Connection, tournament_id: int,
                 round_no: int) -> int:
    sql = "INSERT INTO rounds (tournament_id, round_no) VALUES (?,?)"
    cur = conn.execute(sql, (tournament_id, round_no))
    return cur.lastrowid

def insert_game(conn: sqlite3.Connection, round_id: int,
                white_player_id: int, black_player_id: int) -> int:
    sql = 'INSERT INTO games (round_id, white_player_id, black_player_id) VALUES (?,?,?)'
    cur = conn.execute(sql, (round_id, white_player_id, black_player_id))
    return cur.lastrowid    #game.id

def update_game_result(conn: sqlite3.Connection, game_id: int,
                       result: str) -> int:
    sql = 'UPDATE games SET result = ? WHERE id = ?'
    cur = conn.execute(sql, (result, game_id))
    return None

def fetch_games_for_tournament(conn: sqlite3.Connection, tournament_id: int) -> list [Game]:
    sql = '''SELECT games.white_player_id as white_id,
        games.black_player_id as black_id, games.result, games.id FROM games
        JOIN rounds ON games.round_id = rounds.id WHERE rounds.tournament_id = ?'''
    rows = conn.execute(sql, (tournament_id,)).fetchall()
    game_list = []
    for row in rows:
        g = Game(row["white_id"], row["black_id"], row["result"])
        game_list.append(g)
    return game_list
