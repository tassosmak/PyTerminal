from pycallgraph2 import GlobbingFilter, PyCallGraph, Config
from pycallgraph2.output import GraphvizOutput
from Kernel import flags


output_png="Kernel/src/CallGraph.png"
custom_include=None

"""A call graph generator filtered"""
def Grapher(func):
    def wrapper():
        if flags.EnableIntSoft and '1' in flags.FTU:
            config = Config()
            config.trace_filter = GlobbingFilter(include=custom_include)
            graphviz = GraphvizOutput(output_file=output_png)
            with PyCallGraph(output=graphviz, config=config):
                        func()
        else:
            func()
    return wrapper