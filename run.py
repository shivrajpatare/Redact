import sys
import os
# Add src to python path to allow direct execution
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from src.cli import cli

if __name__ == '__main__':
    cli()
