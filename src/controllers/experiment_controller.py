from typing import List

from src.controllers.exp_info_controller import ExpInfoController
from src.controllers.trial_controller import TrialController
from src.models.entities.trial_result import TrialResult
from src.models.repositories.experiment_config_repository import (
    ExperimentConfigRepository,
)
from src.models.repositories.trial_result_repository import TrialResultRepository


class ExperimentController:
    def __init__(self):

        self.exp_config_repo = ExperimentConfigRepository()
        # self.exp_info_contr = ExpInfoController()
        # self.start_block_name = self.get_start_block()
        self.trial_controller = TrialController()
        # self.trial_result_rep = TrialResultRepository()

    def save_block(
        self,
        save_path: str,
        block_result: List[TrialResult],
        criteria_mastery: bool,
        repetition_count: int,
    ):

        print(save_path)

    def run(self, block_name, save_path):
        criteria_mastery = 0
        repetition_count = 0
        if "test" in block_name:

            block_result = self.trial_controller.run(block_name)
            self.save_block(save_path, block_result, criteria_mastery, repetition_count)
            return 1
        else:
            while not criteria_mastery:

                block_result = self.trial_controller.run(block_name)
                criteria_mastery = (
                    block_result[-1].cumulative == block_result[-1].trials
                )
                self.save_block(
                    save_path, block_result, criteria_mastery, repetition_count
                )
            return 1
