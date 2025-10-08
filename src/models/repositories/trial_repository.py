import csv
import json
from pathlib import Path  # descreve os caminhos dos arquivos
from random import shuffle
from typing import List

from src.models.entities.block_config import BlockConfig
from src.models.entities.screen_stimuli import ScreenStimuli
from src.models.entities.trial import Trial


class TrialRepository:
    def __init__(self, block_path: str, block_config_path: str):
        self.block_config_path = block_config_path
        self.block_path = block_path

    def load_block_config(self) -> BlockConfig:
        with open(self.block_config_path, "r", encoding="utf-8") as f:
            block_config = json.load(f)

        return BlockConfig(**block_config)

    def load_trials(self) -> List[Trial]:
        block_config = self.load_block_config()

        trials = []
        with open(self.block_path, encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            n = 0
            for trial in reader:

                screens_trial = []
                consequences = {}
                comps = trial["comp"].split(",")
                a = comps[0]
                comps = comps[1:]
                shuffle(comps)  # randomizar posição dos comparações
                comps.insert(0, a)
                screen_sample = ScreenStimuli(
                    "sample",
                    (0, 0, 0),
                    trial["sample"].split(":"),
                    [int(c) for c in trial["clickable_sample"].split(",")],
                    trial["sample_sound"],
                    None,
                    block_config.stimuli_size,
                    block_config.sample_pos,
                )

                screen_comps = ScreenStimuli(
                    "comp",
                    (0, 0, 0),
                    comps,
                    [int(c) for c in trial["clickable_comp"].split(",")],
                    None,  # TODO
                    None,  # TODO
                    block_config.stimuli_size,
                    block_config.comps_pos,
                )
                screen_right_consequence = ScreenStimuli(
                    "consequence",
                    (0, 0, 0),
                    trial["img_right"].split(":"),
                    [False],
                    None,  # TODO
                    None,  # TODO
                    block_config.consequence_size,
                    block_config.consequence_pos,
                )
                screen_wrong_consequence = ScreenStimuli(
                    "consequence",
                    (0, 0, 0),
                    trial["img_wrong"].split(":"),
                    [False],
                    None,  # TODO
                    None,  # TODO
                    block_config.consequence_size,
                    block_config.consequence_pos,
                )
                screens_trial.append(screen_sample)
                screens_trial.append(screen_comps)
                consequences[1] = screen_right_consequence
                consequences[0] = screen_wrong_consequence
                n += 1
                trials.append(
                    Trial(
                        id=n,
                        screens_trial=screens_trial,
                        correct_comp=trial["correct_comp"],
                        consequences=consequences,
                        time_right=float(trial["time_right"]),
                        time_wrong=float(trial["time_wrong"]),
                    )
                )

        shuffle(trials)  # randomizar
        return trials
