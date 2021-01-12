"""
Unit and regression test for the molecool package.
"""

# Import package, test suite, and other packages as needed
import molecool
import pytest
import sys
import numpy as np


@pytest.fixture(scope="module")
def methane_molecule():
    symbols = np.array(["C", "H", "H", "H", "H"])
    coordinates = np.array(
        [[1, 1, 1], [2.4, 1, 1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]]
    )
    return symbols, coordinates


def test_build_bond_list_failure(methane_molecule):

    symbols, coordinates = methane_molecule

    with pytest.raises(ValueError):
        molecool.build_bond_list(coordinates, min_bond=-1)


@pytest.mark.skip
def test_build_bond_list():

    coordinates = np.array(
        [[1, 1, 1], [2.4, 1, 1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]]
    )

    bonds = molecool.build_bond_list(coordinates)
    assert len(bonds) == 4

    for bond_length in bonds.values():
        assert bond_length == 1.4


def test_calculate_distance():
    """
    Test that the calculate distance function calculates what we expect
    """
    r1 = np.array([0, 0, 0])
    r2 = np.array([0, 1, 0])

    expected_distance = 1

    observed_distance = molecool.calculate_distance(r1, r2)

    assert expected_distance == observed_distance


def test_molecool_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molecool" in sys.modules
