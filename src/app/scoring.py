
from collections import defaultdict
from .models import Game

Result_points={
	"1-0":(1.0,0.0),
	"0-1":(0.0,1.0),
	"1/2-1/2":(0.5,0.5)
}

def compute_points(games: list[Game]) -> dict[int,float]:
	scores=defaultdict(float)
	for g in games:
                # TODO 1: validate g.result is one of RESULT_POINTS keys
        	# If not, raise ValueError with a useful message.
                
                white_points, black_points = Result_points[g.result]
                scores[g.white_id] += white_points
                scores[g.black_id] += black_points
                
	return dict(scores)

