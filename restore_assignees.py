#!/usr/bin/env python3

import runpy
from pathlib import Path


SCRIPT = Path(__file__).resolve().parent / "generated" / "gitlab_assignee_restore" / "restore_assignees.py"


if __name__ == "__main__":
    runpy.run_path(str(SCRIPT), run_name="__main__")
