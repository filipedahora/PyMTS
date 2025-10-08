import csv
from typing import List

from src.models.entities.trial_result import TrialResult


class TrialResultRepository:
    def __init__(self, path: str):
        self.path = path

    def save(self, results: List[TrialResult]):
        """Salva todas as tentativas de um bloco"""
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")

        for trial in results:
            writer.writerow(
                [
                    trial.trials,
                    trial.block,
                    trial.block_trials,
                    trial.accuracy,
                    trial.cumulative,
                    trial.sample,
                    trial.sample_sound,
                    trial.comps,
                    trial.selected,
                    trial.sample_click_time,
                    trial.comp_click_time,
                    trial.trial_time,
                ]
            )
        print(f"[INFO] Resultados salves em:{self.path}")
