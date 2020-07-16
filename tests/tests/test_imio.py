import os
import pytest

import numpy as np

from tifffile import tifffile

from imio import load, save, utils


@pytest.fixture()
def layer():
    return np.tile(np.array([1, 2, 3, 4]), (10, 1))


@pytest.fixture()
def start_array(layer):
    volume = np.dstack((layer, 2 * layer, 3 * layer, 4 * layer))
    return volume


def test_tiff_io(tmpdir, layer):
    folder = str(tmpdir)
    dest_path = os.path.join(folder, "layer.tiff")
    tifffile.imsave(dest_path, layer)
    reloaded = tifffile.imread(dest_path)
    assert (reloaded == layer).all()


def test_to_tiff_stack(tmpdir, start_array):
    folder = str(tmpdir)
    image_path = os.path.join(folder, "image.tiff")
    save.to_tiff(start_array, image_path)
    reloaded_array = load.load_any(image_path)
    assert (reloaded_array == start_array).all()


def test_to_tiff_series(tmpdir, start_array):
    folder = str(tmpdir)
    save.to_tiff_series(start_array, os.path.join(folder, "start_array"))
    reloaded_array = load.load_any(folder)
    assert (reloaded_array == start_array).all()


def test_load_img_sequence(tmpdir, start_array):
    folder = str(tmpdir.mkdir("sub"))
    save.to_tiff_series(start_array, os.path.join(folder, "start_array"))
    img_sequence_file = tmpdir.join("imgs_file.txt")
    img_sequence_file.write(
        "\n".join(
            [
                os.path.join(folder, fname)
                for fname in sorted(os.listdir(folder))
            ]
        )
    )

    reloaded_array = load.load_any(
        str(img_sequence_file),
        sort_input_file=True,
        load_parallel=True,
        n_free_cpus=0,
    )
    assert (reloaded_array == start_array).all()


def test_to_nii(tmpdir, start_array):  # Also tests load_nii
    folder = str(tmpdir)
    nii_path = os.path.join(folder, "test_array.nii")
    save.to_nii(start_array, nii_path, scale=(1, 1, 1))
    assert (load.load_any(nii_path, as_numpy=True) == start_array).all()


def test_to_nrrd(tmpdir, start_array):  # Also tests load_nrrd
    folder = str(tmpdir)
    nrrd_path = os.path.join(folder, "test_array.nrrd")
    save.to_nrrd(start_array, nrrd_path)
    assert (load.load_any(nrrd_path, as_numpy=True) == start_array).all()


def test_scaling(tmpdir, start_array):
    scale = 3
    shape = (
        start_array.shape[0] * scale,
        start_array.shape[1] * scale,
        start_array.shape[2] * scale,
    )

    folder = str(tmpdir)

    # tiff series
    save.to_tiff_series(start_array, os.path.join(folder, "start_array"))
    reloaded_array = load.load_any(
        folder,
        x_scaling_factor=scale,
        y_scaling_factor=scale,
        z_scaling_factor=scale,
    )
    assert shape == reloaded_array.shape

    # tiff stack
    save.to_tiff(start_array, os.path.join(folder, "image.tif"))
    reloaded_array = load.load_any(
        os.path.join(folder, "image.tif"),
        x_scaling_factor=scale,
        y_scaling_factor=scale,
        z_scaling_factor=scale,
    )
    assert shape == reloaded_array.shape


def test_cant_guess(tmpdir):
    file = str(tmpdir / "data.abc")

    with pytest.raises(NotImplementedError):
        assert load.load_any(file)


def test_scale_z(start_array):
    assert utils.scale_z(start_array, 0.5).shape[0] == start_array.shape[0] / 2
    assert utils.scale_z(start_array, 2).shape[0] == start_array.shape[0] * 2


def test_insufficient_memory(start_array, tmpdir):
    x_scaling_factor = y_scaling_factor = z_scaling_factor = 10 ** 1000
    folder = str(tmpdir)
    save.to_tiff_series(start_array, os.path.join(folder, "start_array"))

    with pytest.raises(utils.ImioLoadException):
        assert load.load_from_folder(
            folder,
            x_scaling_factor=x_scaling_factor,
            y_scaling_factor=y_scaling_factor,
            z_scaling_factor=z_scaling_factor,
        )


def test_get_size_image_from_file_paths(start_array, tmpdir):
    folder = str(tmpdir)
    save.to_tiff_series(start_array, os.path.join(folder, "start_array"))
    shape = start_array.shape
    assert utils.get_size_image_from_file_paths(folder) == {
        "x": shape[2],
        "y": shape[1],
        "z": shape[0],
    }
