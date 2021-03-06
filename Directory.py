import os


class Directory:
    """
A simple container class for traversing directories and extracting files.
"""

    def __init__(self, path):
        self.relativePath = path
        self.files = []
        self.subDirectories = []

    """
    Returns a multiline string-y representation of this subdirectory's contents.
    """

    def __repr__(self):
        return self._repr_recurse(2)

    def _repr_recurse(self, depth):
        lines = ["  " * depth + "+- " + self.relativePath]

        filesDict = self.FileTypeCount()
        for key in sorted(filesDict.keys()):
            lines.append("  " * depth + "  +- " + key +
                         ": " + str(filesDict[key]))

        for subDirectory in self.subDirectories:
            lines.append(subDirectory._repr_recurse(depth + 1))

        return "\n".join(lines)

    """
    Returns a dictionary of file extensions and the number of files of that extension in this directory.

    The file extension is considered to be any text after the final period (.) in the file name. So .tar.gz
    files, for example, have the extension GZ.
    """

    def FileTypeCount(self):
        res = dict()
        for fileName in self.files:
            extension = fileName.split('.')[-1]
            if extension not in res:
                res[extension] = 0
            res[extension] += 1

        return res

    """
    Scan this directory, extract all the files, and recursively create and scan the subdirectories.
    """

    def Scan(self):
        rawList = [f for f in os.listdir(self.relativePath)]

        for item in rawList:
            fullFileName = os.path.normpath(self.relativePath + "/" + item)
            if os.path.isfile(fullFileName):
                self.files.append(item)
            elif os.path.isdir(fullFileName):
                newSubDirectory = Directory(fullFileName)
                self.subDirectories.append(newSubDirectory)

        for subDirectory in self.subDirectories:
            subDirectory.Scan()

    def Files(self):
        res = [os.path.normpath(self.relativePath + "/" + f)
               for f in self.files]
        return res

    def FileNames(self):
        return self.files
