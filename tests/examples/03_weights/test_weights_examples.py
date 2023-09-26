"""Test for examples in 03_weights."""
import runpy
import os
from graphnet.constants import GRAPHNET_ROOT_DIR

EXAMPLE_PATH = os.path.join(GRAPHNET_ROOT_DIR, "examples/03_weights")


def test_01_fit_uniform_weights() -> None:
    """Test for 01_fit_uniform_weights."""
    runpy.run_path(
        os.path.join(EXAMPLE_PATH, "01_fit_uniform_weights.py"),
        run_name="__main__",
    )


def test_02_fit_bjoern_low_weights() -> None:
    """Test for 02_fit_bjoern_low_weights."""
    runpy.run_path(
        os.path.join(EXAMPLE_PATH, "02_fit_bjoern_low_weights.py"),
        run_name="__main__",
    )


if __name__ == "__main__":
    test_01_fit_uniform_weights()
    test_02_fit_bjoern_low_weights()
