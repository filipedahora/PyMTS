from dataclasses import dataclass
from typing import Dict, List

from src.models.entities.screen_stimuli import ScreenStimuli


@dataclass
class Trial:
    id: int
    screens_trial: List[ScreenStimuli]
    consequences: Dict[int, ScreenStimuli]
    correct_comp: str
    time_right: float
    time_wrong: float
