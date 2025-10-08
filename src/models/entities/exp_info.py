import os
from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class ExpInfo:
    experiment: str
    experimenter: str
    participant: str
    blocks: List[str]
    start_block: int
    save_path: str
    date: str
