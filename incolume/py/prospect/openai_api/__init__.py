"""
Principal Module.

Update metadata from version by semver
"""

from tomllib import load
from pathlib import Path

configfile = Path(__file__).parents[4].joinpath("pyproject.toml")
versionfile = Path(__file__).parent.joinpath("version.txt")

with configfile.open('rb') as cfg:
    content = load(cfg)['tool']['poetry']['version']
    versionfile.write_text(f"{content}\n")
__version__ = versionfile.read_text().strip()


if __name__ == '__main__':
    print(__version__)
