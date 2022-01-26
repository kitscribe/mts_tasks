import os
from utils import roundup


class CustomFile:
    """
    A CustomFile class
    Helps to easily get file size and it's extension
    """
    def __init__(self, path: [str, os.PathLike]):
        self._path = os.path.abspath(path)

    @property
    def path(self):
        return self._path

    @property
    def size(self):
        return roundup(os.path.getsize(self._path))

    @property
    def extension(self):
        _, ext = os.path.splitext(self._path)
        return ext
