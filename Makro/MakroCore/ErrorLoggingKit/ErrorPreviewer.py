from time import sleep

from Makro.MakroCore.RendererKit.HighlightKit.align import Align
from Makro.MakroCore.RendererKit.HighlightKit.console import Console
from Makro.MakroCore.RendererKit.HighlightKit.panel import Panel

def ErrorScreen():
    console = Console()
    with console.screen(style="bold white on red") as screen:
        text = Align.center("[blink]PyTerminal Error[/blink]", vertical="middle")
        screen.update(Panel(text))
        sleep(5)