import sys


def test_python_runtime_is_supported():
    """Verify pytest runs with the supported Python runtime."""
    assert sys.version_info >= (3, 12)
