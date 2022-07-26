import pytest
import sys
from pathlib import Path

@pytest.fixture
def wnese():
    pack_dir = str(Path(__file__).parent/"../")
    if pack_dir not in sys.path:
        sys.path.append(pack_dir)
    import wngual
    return wngual