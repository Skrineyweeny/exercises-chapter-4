import numpy as np  # noqa 1045


def test_import_pattern():
    """Ensure we can import class Pattern."""
    from life.life import Pattern  # noqa 1045


def test_pattern_grid():
    """Test if the pattern grid is correctly defined."""
    from life.life import Pattern, glider

    assert np.array_equal(Pattern(glider).grid, glider), \
        "Pattern.grid incorrectly defined"
