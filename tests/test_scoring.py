
from app.models import Game
from app.scoring import compute_points

def test_win_loss():
    games = [Game(white_id=1, black_id=2, result="1-0")]
    assert compute_points(games) == {1: 1.0, 2: 0.0}

def test_draw():
    games = [Game(white_id=1, black_id=2, result="1/2-1/2")]
    assert compute_points(games) == {1: 0.5, 2: 0.5}

def test_multiple_games():
    games = [
        Game(1, 2, "1-0"),        # 1 gets 1
        Game(3, 4, "0-1"),        # 4 gets 1
        Game(1, 3, "1/2-1/2"),    # 1 +0.5, 3 +0.5
    ]
    assert compute_points(games) == {1: 1.5, 2: 0.0, 3: 0.5, 4: 1.0}
