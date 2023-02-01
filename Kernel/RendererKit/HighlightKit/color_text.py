"""
This example demonstrates a simple text highlighter.
"""

from Kernel.RendererKit.HighlightKit.console import Console
from Kernel.RendererKit.HighlightKit.highlighter import RegexHighlighter
from Kernel.RendererKit.HighlightKit.theme import Theme


class Highlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    highlights = [r"(?P<highlight>[\w-])"]

def output(content, args=''):
    theme = Theme({"highlight": args})
    console = Console(highlighter=Highlighter(), theme=theme)

    console.print(content)
