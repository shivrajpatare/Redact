import os

from redact.scanner import Scanner


def test_scanner_yields_non_ignored_files(tmp_path):
    (tmp_path / ".gitignore").write_text("ignored.txt\n")
    (tmp_path / "ignored.txt").write_text("secret stuff")
    (tmp_path / "keep.txt").write_text("normal file")

    scanner = Scanner(str(tmp_path))
    found = {os.path.basename(p) for p in scanner.scan()}

    assert "keep.txt" in found
    assert "ignored.txt" not in found


def test_scanner_always_ignores_git_directory(tmp_path):
    git_dir = tmp_path / ".git"
    git_dir.mkdir()
    (git_dir / "config").write_text("git internals")
    (tmp_path / "app.py").write_text("print('hi')")

    scanner = Scanner(str(tmp_path))
    found = {os.path.basename(p) for p in scanner.scan()}

    assert "app.py" in found
    assert "config" not in found


def test_scanner_respects_gitignore_directory_pattern(tmp_path):
    (tmp_path / ".gitignore").write_text("build/\n")
    build_dir = tmp_path / "build"
    build_dir.mkdir()
    (build_dir / "output.txt").write_text("compiled")
    (tmp_path / "main.py").write_text("print('main')")

    scanner = Scanner(str(tmp_path))
    found = {os.path.basename(p) for p in scanner.scan()}

    assert "main.py" in found
    assert "output.txt" not in found
