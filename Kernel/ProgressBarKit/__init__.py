from Kernel.RendererKit.ProgressBarKit._monitor import TMonitor, TqdmSynchronisationWarning
from Kernel.RendererKit.ProgressBarKit._tqdm_pandas import tqdm_pandas
from Kernel.RendererKit.ProgressBarKit.cli import main  # TODO: remove in v5.0.0
from Kernel.RendererKit.ProgressBarKit.gui import tqdm as tqdm_gui  # TODO: remove in v5.0.0
from Kernel.RendererKit.ProgressBarKit.gui import trange as tgrange  # TODO: remove in v5.0.0
from Kernel.RendererKit.ProgressBarKit.std import (
    TqdmDeprecationWarning, TqdmExperimentalWarning, TqdmKeyError, TqdmMonitorWarning,
    TqdmTypeError, TqdmWarning, tqdm, trange)
from Kernel.RendererKit.ProgressBarKit.version import __version__

__all__ = ['tqdm', 'tqdm_gui', 'trange', 'tgrange', 'tqdm_pandas',
           'tqdm_notebook', 'tnrange', 'main', 'TMonitor',
           'TqdmTypeError', 'TqdmKeyError',
           'TqdmWarning', 'TqdmDeprecationWarning',
           'TqdmExperimentalWarning',
           'TqdmMonitorWarning', 'TqdmSynchronisationWarning',
           '__version__']


def tqdm_notebook(*args, **kwargs):  # pragma: no cover
    """See tqdm.notebook.tqdm for full documentation"""
    from warnings import warn

    from Kernel.RendererKit.ProgressBarKit.notebook import tqdm as _tqdm_notebook
    warn("This function will be removed in tqdm==5.0.0\n"
         "Please use `tqdm.notebook.tqdm` instead of `tqdm.tqdm_notebook`",
         TqdmDeprecationWarning, stacklevel=2)
    return _tqdm_notebook(*args, **kwargs)


def tnrange(*args, **kwargs):  # pragma: no cover
    """
    A shortcut for `tqdm.notebook.tqdm(xrange(*args), **kwargs)`.
    On Python3+, `range` is used instead of `xrange`.
    """
    from warnings import warn

    from Kernel.RendererKit.ProgressBarKit.notebook import trange as _tnrange
    warn("Please use `tqdm.notebook.trange` instead of `tqdm.tnrange`",
         TqdmDeprecationWarning, stacklevel=2)
    return _tnrange(*args, **kwargs)
