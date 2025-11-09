"""Models package.

Import each model module here so that a simple `import src.models` registers
all tables with SQLAlchemy's Base before metadata creation.

Add new models by creating the file (e.g. `order.py`) and adding an import below.
"""

from .user import User
from .item import Item

def load_all_models() -> None:
	"""Explicit hook to ensure all models are imported.

	Can be called if dynamic loading is needed elsewhere.
	"""
	return None