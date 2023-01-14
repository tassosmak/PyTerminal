from time import sleep

from HighlightKit.align import Align
from HighlightKit.console import Console
from HighlightKit.panel import Panel

def ErrorScreen():
    console = Console()
    with console.screen(style="bold white on red") as screen:
        text = Align.center("[blink]PyTerminal Error[/blink]", vertical="middle")
        screen.update(Panel(text))
        sleep(5)