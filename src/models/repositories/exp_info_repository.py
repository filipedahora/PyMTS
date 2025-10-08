import json
import os
from pathlib import Path

from src.models.entities.exp_info import ExpInfo


class ExpInfoRepository:
    def __init__(self, path: str = r"D:\PyMTS\PyMTS\src\data\config\exp_info.json"):
        self.path = path

    def save(self, experiment_info: ExpInfo) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(experiment_info.__dict__, f, indent=2, ensure_ascii=False)

    def load(self):
        with open(self.path, "r", encoding="utf-8") as f:
            experiment_info = json.load(f)

        return ExpInfo(**experiment_info)
