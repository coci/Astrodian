import sys

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class APIGuardian(App):
	BINDINGS = [("q", "quit", "Quit"), ("d", "toggle_dark", "Toggle dark mode")]

	def compose(self) -> ComposeResult:
		yield Header()
		yield Footer()

	def action_toggle_dark(self) -> None:
		self.dark = not self.dark

	def action_quit(self) -> None:
		sys.exit(-1)


if __name__ == "__main__":
	app = APIGuardian()
	app.run()
