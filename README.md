[![Python Version](https://img.shields.io/pypi/pyversions/imio.svg)](https://pypi.org/project/imio)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
[![PyPI](https://img.shields.io/pypi/v/imio.svg)](https://pypi.org/project/imio)
[![Downloads](https://pepy.tech/badge/imio)](https://pepy.tech/project/imio)
[![Wheel](https://img.shields.io/pypi/wheel/imio.svg)](https://pypi.org/project/imio)
[![Development Status](https://img.shields.io/pypi/status/imio.svg)](https://github.com/brainglobe/imio)
[![Tests](https://img.shields.io/github/workflow/status/brainglobe/imio/tests)](
    https://github.com/brainglobe/imio/actions)
[![codecov](https://codecov.io/gh/brainglobe/imio/branch/master/graph/badge.svg?token=M1BXRDJ9V4)](https://codecov.io/gh/brainglobe/imio)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Contributions](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](https://github.com/brainglobe/imio)


# imio
Loading and saving of image data.

### About
The aim of imio is to be a lightweight image loading library for the file types
 supported by [cellfinder](https://github.com/brainglobe/cellfinder), and
 [brainreg](https://github.com/brainglobe/brainreg).

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

## Contributing
Contributions to imio are more than welcome. Please see the [contributing guide](https://github.com/brainglobe/.github/blob/main/CONTRIBUTING.md).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://adamltyson.com"><img src="https://avatars.githubusercontent.com/u/13147259?v=4?s=100" width="100px;" alt="Adam Tyson"/><br /><sub><b>Adam Tyson</b></sub></a><br /><a href="https://github.com/brainglobe/imio/commits?author=adamltyson" title="Code">💻</a> <a href="#infra-adamltyson" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-adamltyson" title="Maintenance">🚧</a> <a href="https://github.com/brainglobe/imio/commits?author=adamltyson" title="Tests">⚠️</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!