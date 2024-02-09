from warnings import warn

warn(
    "imio has merged into brainglobe-utils as a submodule."
    "To remain up to date, please install brainglobe-utils and use the image_io submodule:"
    "https://github.com/brainglobe/brainglobe-utils",
    DeprecationWarning,
)

__author__ = "Charly Rousseau, Adam Tyson"
__version__ = "0.2.4"

from imio.load import *
from imio.save import *
from imio.utils import *
