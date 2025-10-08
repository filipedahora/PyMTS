from src.models.entities.screen_stimuli import ScreenStimuli
from src.views.screen_view import ScreenView


class ScreenController:
    def __init__(self):

        self.screen_view = ScreenView()

    def run_screen(self, screen_model: ScreenStimuli, time: float):

        self.screen_view.update_info(screen_model, time)
        return self.screen_view.run()
