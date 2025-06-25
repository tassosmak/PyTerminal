"""
This example demonstrates a simple text highlighter.
"""

from Makro.MakroCore.RendererKit.HighlightKit.console import Console
from Makro.MakroCore.RendererKit.HighlightKit.highlighter import RegexHighlighter
from Makro.MakroCore.RendererKit.HighlightKit.theme import Theme


class Highlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    highlights = [r"(?P<highlight>[\w-])"]

def output(content, args=''):
    theme = Theme({"highlight": args})
    console = Console(highlighter=Highlighter(), theme=theme)

    console.print(content)
