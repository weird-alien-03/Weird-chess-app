
-- schema.sql
-- Swiss MVP: players, tournaments, rounds, games

CREATE TABLE IF NOT EXISTS players (
  id      INTEGER PRIMARY KEY AUTOINCREMENT,
  name    TEXT    NOT NULL UNIQUE,
  rating  INTEGER,
  active  INTEGER NOT NULL DEFAULT 1 CHECK (active IN (0, 1))
);

CREATE TABLE IF NOT EXISTS tournaments (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  name          TEXT    NOT NULL,
  created_at    TEXT    NOT NULL DEFAULT (datetime('now')),
  rounds_planned INTEGER NOT NULL CHECK (rounds_planned > 0)
);

CREATE TABLE IF NOT EXISTS rounds (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  tournament_id INTEGER NOT NULL,
  round_no      INTEGER NOT NULL CHECK (round_no > 0),

  FOREIGN KEY (tournament_id) REFERENCES tournaments(id) ON DELETE CASCADE,
  UNIQUE (tournament_id, round_no)
);

CREATE TABLE IF NOT EXISTS games (
  id              INTEGER PRIMARY KEY AUTOINCREMENT,
  round_id        INTEGER NOT NULL,
  white_player_id INTEGER NOT NULL,
  black_player_id INTEGER NOT NULL,

  -- store result as text for now: '1-0', '0-1', '1/2-1/2', 'BYE'
  result          TEXT,

  FOREIGN KEY (round_id) REFERENCES rounds(id) ON DELETE CASCADE,
  FOREIGN KEY (white_player_id) REFERENCES players(id),
  FOREIGN KEY (black_player_id) REFERENCES players(id),

  CHECK (white_player_id <> black_player_id),
  CHECK (result IN ('1-0', '0-1', '1/2-1/2', 'BYE') OR result IS NULL)
);
