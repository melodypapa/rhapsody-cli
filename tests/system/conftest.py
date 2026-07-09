"""System test configuration."""

import sys
from pathlib import Path

# Add unit directory to Python path so imports from unit tests work
sys.path.insert(0, str(Path(__file__).parent.parent / "unit"))
