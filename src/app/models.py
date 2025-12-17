
from dataclasses import dataclass

@dataclass(frozen=True)

class Game:
	white_id: int
	black_id: int
	result: str 	#'1-0', '0-1', '1/2-1/2'
