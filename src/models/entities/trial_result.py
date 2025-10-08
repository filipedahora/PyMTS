from dataclasses import dataclass
from typing import List


@dataclass
class TrialResult:
    block: str  # nome do bloco
    trials: int
    block_trials: int
    accuracy: int
    cumulative: int
    sample: str
    sample_sound: str
    comps: str
    selected: str
    sample_click_time: float
    comp_click_time: float
    trial_time: float
