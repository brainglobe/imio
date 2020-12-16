[![Python Version](https://img.shields.io/pypi/pyversions/imio.svg)](https://pypi.org/project/imio)
[![PyPI](https://img.shields.io/pypi/v/imio.svg)](https://pypi.org/project/imio)
[![Downloads](https://pepy.tech/badge/imio)](https://pepy.tech/project/imio)
[![Wheel](https://img.shields.io/pypi/wheel/imio.svg)](https://pypi.org/project/imio)
[![Development Status](https://img.shields.io/pypi/status/imio.svg)](https://github.com/brainglobe/imio)
[![Tests](https://img.shields.io/github/workflow/status/brainglobe/imio/tests)](
    https://github.com/brainglobe/imio/actions)
[![Coverage Status](https://coveralls.io/repos/github/brainglobe/imio/badge.svg?branch=master)](https://coveralls.io/github/brainglobe/imio?branch=master)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/brainglobe/imio)


# imio
Loading and saving of image data.

### About
The aim of imio is to be a lightweight image loading library for the file types
 supported by [cellfinder](https://github.com/brainglobe/cellfinder), and
 [brainreg](https://github.com/brainglobe/brainreg). It is an update to 
 [brainio](https://github.com/adamltyson/brainio).

#### Supports loading of:
* Tiff stack `+`
* Tiff series (from a directory, a text file or a list of file paths). `*+`
* nrrd
* nifti (`.nii` & `.nii.gz`)

`*` Supports loading in parallel for speed

`+` Suports scaling on loading. E.g. downsampling to load images bigger than the 
available RAM

#### Supports saving of:
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
save.to_nii(volume, "image.nii")
reloaded_volume = load.load_any("image.nii")
(volume == reloaded_volume).all() # True

# repeat, saving as a nrrd file
save.to_nrrd(volume, "image.nrrd")
reloaded_volume = load.load_any("image.nrrd")
(volume == reloaded_volume).all() # True
```

