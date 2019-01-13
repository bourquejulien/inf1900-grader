from urwid import Filler

from src.views.base.buffer import Controller, Signal
from src.views.base.hydra import HydraWidget
from src.views.base.tui import TUI
from src.views.panels.assemble import AssemblePanel
from src.views.panels.clone import ClonePanel
from src.views.panels.grade import GradePanel
from src.views.panels.mail import MailPanel


@Signal("on_swap")
class MainPanel(HydraWidget, Controller):

    def __init__(self):
        super().__init__(info="Welcome to INF1900 interactive grading tool!", align="center")

        self.add_views([
            ("c", "Clone", ClonePanel()),
            ("g", "Grade", GradePanel()),
            ("a", "Assemble", AssemblePanel()),
            ("m", "Mail", MailPanel())
        ])

        self.add_actions([
            ("q", "red_head", "Quit", TUI.quit),
        ])

        self.root = Filler(self, valign="bottom")

    def add_views(self, views):
        heads = []
        for letter, hint, view, in views:
            view.connect("on_quit", self.restore)
            heads.append((letter, "blue_head", hint, self.swap_view, {"view": view, "hint": hint}))

        self.add_heads(heads)

    def add_actions(self, actions: list):
        self.add_heads(actions)

    def swap_view(self, view, hint):
        self.emit("on_swap", view, hint)

    def restore(self, *kargs):
        self.emit("on_swap", self, "")