from pycallgraph2 import GlobbingFilter, PyCallGraph, Config
from pycallgraph2.output import GraphvizOutput
from Kernel import flags

def call_graph_filtered(function_, output_png=f"Kernel/src/CallGraph.png", custom_include=None):
    if flags.EnableIntSoft:
        """A call graph generator filtered"""
        config = Config()
        config.trace_filter = GlobbingFilter(include=custom_include)
        graphviz = GraphvizOutput(output_file=output_png)
        with PyCallGraph(output=graphviz, config=config):
                    function_()
    else:
        function_()