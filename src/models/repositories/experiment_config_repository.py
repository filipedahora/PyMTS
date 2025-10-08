import json
from pathlib import Path

from src.models.entities.experiment_config import ExperimentConfig


class ExperimentConfigRepository:
    def __init__(self):
        self.experiment_config_path = (
            Path(__file__).parent.parent.parent / "data/config/experiment.json"
        )

    def load_experiment_config(self):
        with open(self.experiment_config_path, "r", encoding="utf-8") as f:
            experiment_config = json.load(f)

        return ExperimentConfig(**experiment_config)
