[![Python Version](https://img.shields.io/pypi/pyversions/imio.svg)](https://pypi.org/project/imio)
[![PyPI](https://img.shields.io/pypi/v/imio.svg)](https://pypi.org/project/imio)
[![Downloads](https://pepy.tech/badge/imio)](https://pepy.tech/project/imio)
[![Wheel](https://img.shields.io/pypi/wheel/imio.svg)](https://pypi.org/project/imio)
[![Development Status](https://img.shields.io/pypi/status/imio.svg)](https://github.com/adamltyson/imio)
[![Travis](https://img.shields.io/travis/com/adamltyson/imio?label=Travis%20CI)](
    https://travis-ci.com/adamltyson/imio)
[![Coverage Status](https://coveralls.io/repos/github/adamltyson/imio/badge.svg?branch=master)](https://coveralls.io/github/adamltyson/imio?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)]()


# imio
Loading and saving of image data. Data can be scaled upon loading to save RAM for very large images.

Supports loading of:
* Tiff stack
* Tiff series (from a directory, a text file or a list of file paths). Can optionally load in parallel.
* nrrd
* nifti (`.nii` & `.nii.gz`)

Supports saving of:
* Tiff stack
* Tiff series
* nifti 

### To install
```bash
pip install imio
```

### To use
```python
import numpy as np
from imio import load, save

# make a 3D image volume
layer = np.tile(np.array([1, 2, 3, 4]), (4, 1))
volume = np.dstack((layer, 2 * layer, 3 * layer, 4 * layer))

# save as tiff stack, reload and check it's correct
save.to_tiff(volume, "image.tiff")
reloaded_volume = load.load_any("image.tiff")
(volume == reloaded_volume).all() # True

# repeat, saving as a series of 2D tiffs
save.to_tiff_series(volume, "image")
reloaded_volume = load.load_any("./")
(volume == reloaded_volume).all() # True

# repeat, saving as a nifti file
save.to_nii(volume, "image")
reloaded_volume = load.load_any("./")
(volume == reloaded_volume).all() # True
```

