from src.controllers.exp_info_controller import ExpInfoController
from src.controllers.experiment_controller import ExperimentController
from src.controllers.trial_controller import TrialController


def start():

    exp_info_controller = ExpInfoController()
    exp_controller = ExperimentController()
    exp_info = exp_info_controller.load_info()
    exp_info = exp_info_controller.record_info(exp_info.__dict__)

    print(exp_info)
    # rodando o experimento
    current = exp_info["start_block"]

    continua = 1
    while continua:

        result = exp_controller.run(exp_info["blocks"][current], exp_info["save_path"])
        current += result
        continuar = len(exp_info["blocks"]) <= current
