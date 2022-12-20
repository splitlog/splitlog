from pathlib import Path

import pytest

from splitlog.__main__ import _Arguments, _parse_args


def test_parse_args_no_args_works():
    actual = _parse_args([])

    expected = _Arguments(
        output_folder=Path("out"),
        input_file=None,
        verbose=False,
        version=False,
    )

    assert actual == expected


def test_parse_args_help_raises():
    with pytest.raises(SystemExit):
        _parse_args(["--help"])


def test_parse_args_infile_works():
    actual = _parse_args(["--input-file", "yarn-logs.txt"])

    expected = _Arguments(
        output_folder=Path("out"),
        input_file=Path("yarn-logs.txt"),
        verbose=False,
        version=False,
    )

    assert actual == expected


def test_parse_args_infile_outdir_works():
    actual = _parse_args(["--input-file", "yarn-logs.txt", "custom-out"])

    expected = _Arguments(
        output_folder=Path("custom-out"),
        input_file=Path("yarn-logs.txt"),
        verbose=False,
        version=False,
    )

    assert actual == expected


def test_parse_args_outdir_infile_works():
    actual = _parse_args(["custom-out", "--input-file", "yarn-logs.txt"])

    expected = _Arguments(
        output_folder=Path("custom-out"),
        input_file=Path("yarn-logs.txt"),
        verbose=False,
        version=False,
    )

    assert actual == expected


def test_parse_args_verbose_works():
    actual = _parse_args(["--verbose"])

    expected = _Arguments(
        output_folder=Path("out"),
        input_file=None,
        verbose=True,
        version=False,
    )

    assert actual == expected


def test_parse_args_version_works():
    actual = _parse_args(["--version"])

    expected = _Arguments(
        output_folder=Path("out"),
        input_file=None,
        verbose=False,
        version=True,
    )

    assert actual == expected
