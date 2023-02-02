from typing import Any


def load_ipython_extension(ip: Any) -> None:  # pragma: no cover
    # prevent circular import
    from RendererKit.HighlightKit.pretty import install
    from RendererKit.HighlightKit.traceback import install as tr_install

    install()
    tr_install()
