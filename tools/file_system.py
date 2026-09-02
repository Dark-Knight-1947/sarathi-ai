import os
from pathlib import Path

def open_file_or_folder(path: str):
    """Open a file or folder on the computer."""
    path = Path(path)

    if not path.exists():
        return f"I couldn't find {path}."

    os.startfile(path)
    return f"Opened {path}."