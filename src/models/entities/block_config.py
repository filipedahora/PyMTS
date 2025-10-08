from dataclasses import dataclass
from typing import List


@dataclass
class BlockConfig:
    delay: int  # se vai ser com delay
    ITI: float
    stimuli_size: List[int]
    consequence_size: List[int]
    sample_pos: List[int]
    comps_pos: List[List[int]]
    consequence_pos: List[List[int]]
    instruction: str
    instruction_size: List[int]
