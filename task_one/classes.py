import os
from utils import roundup
import typing


class CustomFile:
    """
    A CustomFile class
    Helps to easily get file size and it's extension
    """
    def __init__(self, path: typing.Union[str, os.PathLike]) -> None:
        self._path = os.path.abspath(path)

    @property
    def path(self) -> typing.Union[str, os.PathLike]:
        return self._path

    @property
    def size(self) -> int:
        return roundup(os.path.getsize(self._path))

    @property
    def extension(self) -> str:
        _, ext = os.path.splitext(self._path)
        return ext
