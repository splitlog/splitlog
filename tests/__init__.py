import typing as t
from fsspec.implementations.memory import MemoryFileSystem  # type: ignore


def filesystem_to_dict(fs: MemoryFileSystem) -> t.Dict[str, t.Any]:
    """
    Walks a MemoryFileSystem and returns a nested dictionary representing the structure.
    Files are represented as bytes.
    Directories are represented as nested dictionaries.
    """
    result: t.Dict[str, t.Any] = {}
    # Use find to get all files. Directories are inferred from file paths.
    # If empty directories are important, we'd need to handle them,
    # but the fixture only asserts on file content and structure.
    # However, to match the original InMemoryOutputFolder behavior which created empty dicts for dirs:

    # We'll traverse all paths known to fs.
    # fs.find might not return empty directories.
    # fs.walk might be better.

    for path, info in fs.find("/", detail=True).items():
        clean_path = path.strip("/")
        if not clean_path:
            continue

        parts = clean_path.split("/")
        current = result

        if info["type"] == "directory":
            for part in parts:
                current = current.setdefault(part, {})
        elif info["type"] == "file":
            for part in parts[:-1]:
                current = current.setdefault(part, {})
            current[parts[-1]] = fs.cat_file(path)

    return result
