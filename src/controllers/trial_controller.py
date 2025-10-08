from pathlib import Path
from typing import List

from src.controllers.screen_controller import ScreenController
from src.models.entities.screen_stimuli import ScreenStimuli
from src.models.entities.trial import Trial
from src.models.entities.trial_result import TrialResult
from src.models.repositories.trial_repository import TrialRepository
from src.views.screen_view import ScreenView

# apresenta o view dos estímulos modelo
# pega a interação da view sample
# apresenta o view comp
# pega a interação comp
# decide e apresenta a view das consequência


class TrialController:
    def __init__(self):

        self.block_path = None
        self.config_block_path = None
        self.trial_repository = None
        self.trials_block = None

    def update_block(self, block_name):
        self.block_path = (
            Path(__file__).parent.parent / r"data\config\blocks" / block_name
        )
        self.block_path = self.block_path.with_suffix(".csv")
        self.config_block_path = (
            Path(__file__).parent.parent / r"data\config\blocks" / block_name
        )
        self.config_block_path = self.config_block_path.with_suffix(".json")
        self.trial_repository = TrialRepository(self.block_path, self.config_block_path)
        self.trials_block = self.trial_repository.load_trials()

    def run(self, block_name) -> List[TrialResult]:
        self.update_block(block_name)
        screen_controller = ScreenController()
        block = []
        trials_number = 0
        cumulative = 0

        for trial in self.trials_block[:3]:
            trial_data = {}
            accuracy = 0

            for screen in trial.screens_trial:
                time = None

                (
                    trial_data[screen.screen_type],
                    trial_data[screen.screen_type + "_time"],
                ) = screen_controller.run_screen(screen, time)

            if trial.consequences:
                accuracy = trial_data["comp"] == trial.correct_comp

                time = None
                if accuracy:
                    time = trial.time_right
                    cumulative += 1
                else:
                    time = trial.time_wrong

                screen_controller.run_screen(trial.consequences[int(accuracy)], time)

            trials_number += 1
            block.append(
                TrialResult(
                    block=block_name,
                    trials=trials_number,
                    block_trials=0,
                    accuracy=accuracy,
                    cumulative=cumulative,
                    sample=trial_data["sample"],
                    sample_sound=None,
                    comps=trial.screens_trial[1],
                    selected=trial_data["comp"],
                    sample_click_time=round(trial_data["sample_time"], 3),
                    comp_click_time=round(trial_data["comp_time"], 3),
                    trial_time=None,
                )
            )

        return block
