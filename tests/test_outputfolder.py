from pathlib import Path
from tempfile import TemporaryDirectory

import pytest

from splitlog.outputfolder import new_output_folder


def test_outputfolder_enter_exist_raises():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir)
        subject = new_output_folder(path)
        with pytest.raises(FileExistsError):
            subject.__enter__()


def test_outputfolder_enter_parent_not_exists_raises():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "nonexistent" / "out"
        subject = new_output_folder(path)
        with pytest.raises(FileNotFoundError):
            subject.__enter__()


def test_outputfolder_enter_works():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "out"
        with new_output_folder(path):
            pass

        assert path.exists()
        assert path.is_dir()


def test_outputfolder_mkdir_works():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "out"
        with new_output_folder(path) as of:
            of.mkdir(of.root / "dir")

        expected = path / "dir"
        assert expected.exists()
        assert expected.is_dir()


def test_outputfolder_double_mkdir_raises():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "out"
        with new_output_folder(path) as of:
            of.mkdir(of.root / "dir")
            with pytest.raises(FileExistsError):
                of.mkdir(of.root / "dir")


def test_outputfolder_mkdir_missing_parent_raises():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "out"
        with new_output_folder(path) as of:
            with pytest.raises(FileNotFoundError):
                of.mkdir(of.root / "dir" / "subdir")


def test_outputfolder_create_works():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "out"
        with new_output_folder(path) as of:
            with of.create(of.root / "file.txt") as f:
                f.write(b"Hello World!")

        expected = path / "file.txt"
        assert expected.exists()
        assert expected.is_file()
        assert expected.read_bytes() == b"Hello World!"


def test_outputfolder_double_create_raises():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "out"
        with new_output_folder(path) as of:
            with of.create(of.root / "file.txt"):
                pass
            with pytest.raises(FileExistsError):
                with of.create(of.root / "file.txt"):
                    pytest.fail("Should never reach with block")


def test_outputfolder_create_missing_parent_raises():
    with TemporaryDirectory("splitlog_tests") as tmpdir:
        path = Path(tmpdir) / "out"
        with new_output_folder(path) as of:
            with pytest.raises(FileNotFoundError):
                with of.create(of.root / "subdir" / "file.txt"):
                    pytest.fail("Should never reach with block")
