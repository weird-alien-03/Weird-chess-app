

# src/app/repo.py
from __future__ import annotations
import sqlite3
from pathlib import Path

def connect(db_path: str | Path) -> sqlite3.Connection:
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")  # must be enabled per-connection
    return conn

def create_schema(conn: sqlite3.Connection) -> None:
    sql = (Path(__file__).resolve().parents[2] / "schema.sql").read_text(encoding="utf-8")
    conn.executescript(sql)
    conn.commit()
