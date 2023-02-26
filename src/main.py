import sys

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Input, Button, Static


class NavBar(Static):
	def on_button_pressed(self, event: Button.Pressed) -> None:
		"""Event handler called when a button is pressed."""
		if event.button.id == "send":
			data = self.query_one("#url").value
			with open("/Users/odin/Desktop/t.txt", "w+") as file:
				file.write(f"{data}")

	def compose(self) -> ComposeResult:
		yield Input(placeholder="Method", id="method")
		yield Input(placeholder="Enter the url", id="url")
		yield Button("Send", id="send")


class APIGuardian(App):
	CSS_PATH = "../assets/style.css"
	BINDINGS = [("q", "quit", "Quit"), ("d", "toggle_dark", "Toggle dark mode")]

	def compose(self) -> ComposeResult:
		yield Header()
		yield Footer()
		yield Container(NavBar())

	def action_toggle_dark(self) -> None:
		self.dark = not self.dark

	def on_button_pressed(self, event: Button.Pressed) -> None:
		"""Event handler called when a button is pressed."""
		if event.button.id == "send":
			print("send request")

	def action_quit(self) -> None:
		sys.exit(-1)


if __name__ == "__main__":
	app = APIGuardian()
	app.run()
