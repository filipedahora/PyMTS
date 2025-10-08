from dataclasses import dataclass
from typing import List


@dataclass
class ExperimentConfig:
    screen_color: List[int]
    volume: float
    start_block: int
    blocks: List[str]
    repetitions: List[int]
    criteria: List[int]
