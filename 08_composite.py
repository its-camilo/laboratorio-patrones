class FileSystemItem:
    def __init__(self, name: str):
        self.name = name

    def get_size(self) -> int:
        raise NotImplementedError


class File(FileSystemItem):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self._size = size

    def get_size(self) -> int:
        return self._size


class Folder(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem):
        self.children.append(item)

    def get_size(self) -> int:
        return sum(child.get_size() for child in self.children)


root = Folder("proyecto")
root.add(File("README.md", 2))
src = Folder("src")
src.add(File("main.py", 10))
src.add(File("utils.py", 5))
root.add(src)
print(root.get_size())  # 17 (se trata igual un archivo que una carpeta)
