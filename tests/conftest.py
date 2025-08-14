import sys
from pathlib import Path

# Ensure the repository root is on the Python path so that ``src`` can be imported
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
