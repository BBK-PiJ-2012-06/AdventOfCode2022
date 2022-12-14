from __future__ import annotations

class Directory:
    def __init__(self, name: str, parent: Directory) -> None:
        self.name = name
        self.contents = []
        self.parent = parent

    def append(self, fileOrDir) -> None:
        self.contents.append(fileOrDir)

    def getSize(self) -> int:
        size = 0
        for item in self.contents:
            size += item.getSize()
        return size

class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size

    def getSize(self) -> int:
        return self.size   

