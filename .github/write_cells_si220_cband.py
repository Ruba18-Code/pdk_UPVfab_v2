"""Write docs."""

import inspect

from upvfab.sin300.cband import _cells as cells
from upvfab.sin300.cband.config import PATH

filepath = PATH.repo / "docs" / "cells_sin300_cband.rst"

skip = {}

skip_plot: tuple[str, ...] = ("",)
skip_settings: tuple[str, ...] = ()


with open(filepath, "w+") as f:
    f.write(
        """

Cells Si SOI 220nm Cband
=============================
"""
    )

    for name in sorted(cells.keys()):
        if name in skip or name.startswith("_"):
            continue
        print(name)
        sig = inspect.signature(cells[name])
        kwargs = ", ".join(
            [
                f"{p}={repr(sig.parameters[p].default)}"
                for p in sig.parameters
                if isinstance(sig.parameters[p].default, int | float | str | tuple)
                and p not in skip_settings
            ]
        )
        if name in skip_plot:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: upvfab.sin300.cband.cells.{name}

"""
            )
        else:
            f.write(
                f"""

{name}
----------------------------------------------------

.. autofunction:: upvfab.sin300.cband.cells.{name}

.. plot::
  :include-source:

  import upvfab

  c = upvfab.sin300.cband.cells.{name}({kwargs}).dup()
  c.draw_ports()
  c.plot()

"""
            )
