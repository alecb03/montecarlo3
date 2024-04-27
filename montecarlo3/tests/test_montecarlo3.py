"""
Unit and regression test for the montecarlo3 package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import montecarlo3


def test_montecarlo3_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "montecarlo3" in sys.modules
