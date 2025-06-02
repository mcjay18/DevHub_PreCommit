#!/usr/bin/env python3
from __future__ import annotations

import os
import sys


__version__ = "1.0.1"



def main():
    # Define the expected README filename
    readme_files = ["README.md", "README.rst", "README.txt", "README"]

    # Check if any of the expected README files exist
    if not any(os.path.isfile(readme) for readme in readme_files):
        print("No README file found! Please add a README.md or equivalent file.")
        return 1  # Non-zero exit code indicates failure

    for readme in readme_files:
        try:
            with open(readme, "r") as f:
                content = f.read()
                if "TODO" in content:
                    print("Error: README contains 'TODO' keyword.")
                    return 1
        except FileNotFoundError:
            print(
                f"Error: {readme} file not found! Checking for other relevant files equivalent file."
            )

    print("README file exists!")
    return 0  # Zero exit code indicates success


if __name__ == "__main__":
    sys.exit(main())
