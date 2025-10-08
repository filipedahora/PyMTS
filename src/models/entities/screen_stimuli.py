from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ScreenStimuli:
    screen_type: str
    screen_color: Tuple
    images: List[str]
    clickable: List[int]
    sounds: List[str]
    texts: List[str]
    images_size: List[int]
    images_pos: List[List[int]]
