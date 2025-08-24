import gzip
from filecmp import dircmp
from pathlib import Path
from shutil import copyfileobj, unpack_archive

import pytest


def pytest_generate_tests(metafunc: pytest.Metafunc):
    if "testcase" in metafunc.fixturenames:
        testcases_dir = Path(__file__).parent / "testcases"
        metafunc.parametrize(
            "testcase", [x for x in testcases_dir.iterdir() if x.is_dir()]
        )


def assert_dircmp_same(dcmp: dircmp):
    assert dcmp.left_only == []
    assert dcmp.right_only == []
    assert dcmp.diff_files == []

    for subdir in dcmp.subdirs.values():
        assert_dircmp_same(subdir)


def test_main(testcase: Path, tmp_path: Path):
    expected_output_tarball = testcase / "expected-output.tgz"
    input_gz = testcase / "input.txt.gz"

    expected = tmp_path / "expected"
    input_file = tmp_path / "input.txt"
    actual = tmp_path / "actual"

    expected.mkdir(mode=0o700)
    actual.mkdir(mode=0o700)

    with gzip.open(input_gz, "rb") as f_in:
        with input_file.open("xb") as f_out:
            copyfileobj(f_in, f_out)

    unpack_archive(expected_output_tarball, expected)

    from splitlog.__main__ import main

    main(["--input-file", str(input_file), str(actual / "output")])

    dcmp = dircmp(expected, actual)

    dcmp.report()

    assert_dircmp_same(dcmp)
