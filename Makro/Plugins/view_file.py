from textual.widgets import DirectoryTree, Footer, Header, Static
from textual.containers import Container, Vertical
from textual.app import App, ComposeResult
from textual.reactive import var
from textual import events

from src import utils
utils.add_depend(str(utils.sys.argv[1]))
from Makro.MakroCore.RendererKit.HighlightKit.traceback import Traceback
from Makro.MakroCore.RendererKit.HighlightKit.syntax import Syntax

import sys



class CodeBrowser(App):
    """Textual code browser app."""

    CSS_PATH = "src/view_file.css"
    BINDINGS = [
        ("f", "toggle_files", "Toggle Files"),
        ("q", "quit", "Quit"),
    ]

    show_tree = var(True)

    def watch_show_tree(self, show_tree: bool) -> None:
        """Called when show_tree is modified."""
        self.set_class(show_tree, "-show-tree")

    def compose(self) -> ComposeResult:
        """Compose our UI."""
        path = "./" if len(sys.argv) < 2 else sys.argv[1]
        yield Header()
        yield Container(
            DirectoryTree(path, id="tree-view"),
            Vertical(Static(id="code", expand=True), id="code-view"),
        )
        yield Footer()

    def on_mount(self, event: events.Mount) -> None:
        self.query_one(DirectoryTree).focus()

    def on_directory_tree_file_selected(
        self, event: DirectoryTree.FileSelected
    ) -> None:
        """Called when the user click a file in the directory tree."""
        event.stop()
        code_view = self.query_one("#code", Static)
        try:
            syntax = Syntax.from_path(
                event.path,
                line_numbers=True,
                word_wrap=False,
                indent_guides=True,
                theme="github-dark",
            )
        except Exception:
            code_view.update(Traceback(theme="github-dark", width=None))
            self.sub_title = "ERROR"
        else:
            code_view.update(syntax)
            self.query_one("#code-view").scroll_home(animate=False)
            self.sub_title = event.path

    def action_toggle_files(self) -> None:
        """Called in response to key binding."""
        self.show_tree = not self.show_tree


if __name__ == "__main__":
    CodeBrowser().run()