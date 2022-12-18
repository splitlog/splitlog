import types
import typing as t
from pathlib import Path

from splitlog import OutputFolder
from splitlog.outputfolder import BinWriter


class ByteArrayWriter(BinWriter):
    def __init__(self, buffer: bytearray):
        self._value = buffer

    def write(self, b: bytes) -> int:
        before = len(self._value)
        self._value.extend(b)
        return len(self._value) - before

    def __exit__(
        self,
        exc: t.Union[t.Type[BaseException], None],
        value: t.Union[BaseException, None],
        tb: t.Union[types.TracebackType, None],
    ) -> None:
        return None


class InMemoryOutputFolder(OutputFolder):
    def __init__(self):
        self._store = dict()

    @property
    def output(self):
        return self._store

    @property
    def root(self) -> Path:
        return Path()

    def mkdir(self, path: Path) -> None:
        assert not path.is_absolute(), f"Path {path} must be relative"
        cur = self._store
        for component in path.parent.parts:
            cur = cur.get(component)
            if cur is None:
                raise FileNotFoundError(f"{path.parent}")
        if path.name in cur:
            raise FileExistsError(f"{path}")
        cur[path.name] = dict()

    def create(self, path: Path) -> BinWriter:
        assert not path.is_absolute(), f"Path {path} must be relative"
        cur = self._store
        for component in path.parent.parts:
            cur = cur.get(component)
            if cur is None:
                raise FileNotFoundError(f"{path.parent}")
        if path.name in cur:
            raise FileExistsError(f"{path}")
        buffer = bytearray()
        cur[path.name] = buffer
        return ByteArrayWriter(buffer)

    def __exit__(
        self,
        exc: t.Union[t.Type[BaseException], None],
        value: t.Union[BaseException, None],
        tb: t.Union[types.TracebackType, None],
    ) -> None:
        return None
