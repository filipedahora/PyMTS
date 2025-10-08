from datetime import datetime
from pathlib import Path
from typing import Dict

from src.models.entities.exp_info import ExpInfo
from src.models.repositories.exp_info_repository import ExpInfoRepository
from src.views.exp_info_view import ExpInfoView


class ExpInfoController:
    def __init__(self):

        self.exp_info = self.load_info()
        self.data = self.exp_info.__dict__
        self.exp_info_view = ExpInfoView(self.on_submit, self.exp_info)
        self.exp_info_view.mainloop()

    def load_info(self) -> ExpInfo:

        exp_info_rep = ExpInfoRepository()
        data = exp_info_rep.load()

        return data

    def on_submit(self, data: Dict):
        self.data = data

    def record_info(self, data: Dict) -> Dict:

        self.data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.data["blocks"] = self.exp_info.blocks
        experiment_info = ExpInfo(**self.data)
        experiment_info_repository = ExpInfoRepository()
        experiment_info_repository.save(experiment_info)

        return data
