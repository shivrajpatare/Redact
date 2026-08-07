import os
import pathspec
from typing import Iterator

class Scanner:
    def __init__(self, root_path: str, ignores: list[str] = None):
        self.root_path = os.path.abspath(root_path)
        self.ignore_spec = self._load_gitignore()
        if ignores:
             self.ignore_spec += pathspec.PathSpec.from_lines('gitwildmatch', ignores)

    def _load_gitignore(self) -> pathspec.PathSpec:
        gitignore_path = os.path.join(self.root_path, '.gitignore')
        lines = []
        if os.path.exists(gitignore_path):
            with open(gitignore_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        
        # Always add .git to ignores
        lines.append('.git/')
        return pathspec.PathSpec.from_lines('gitwildmatch', lines)

    def scan(self) -> Iterator[str]:
        """Yields absolute paths of files to scan."""
        for root, dirs, files in os.walk(self.root_path):
            # 1. Filter directories in-place to prevent walking ignored dirs
            relative_root = os.path.relpath(root, self.root_path)
            if relative_root == '.':
                relative_root = ''
                
            # We must iterate a copy because we modify 'dirs'
            for d in list(dirs):
                path_to_check = os.path.join(relative_root, d)
                # Add trailing slash for directory matching
                if self.ignore_spec.match_file(path_to_check + '/'):
                    dirs.remove(d)
            
            # 2. Yield valid files
            for f in files:
                rel_path = os.path.join(relative_root, f)
                if not self.ignore_spec.match_file(rel_path):
                    yield os.path.join(root, f)
