class Hard_disk:

    def __init__(self, _size: float):
        self.size = _size
        self.files = {}  # key= name, val= size of file

    def used_space(self):
        """return used space in disk"""
        return sum(self.files.values())

    def free_space(self):
        """return the free space in disk"""
        return self.size - self.used_space()

    def add_file(self, name_file, size_file):
        """add file to disk if is not exist or have free space"""

        if name_file in self.files:
            print("The file exist")
            return False
        if self.free_space() >= size_file > 0:
            self.files[name_file] = size_file
            return True
        else:
            print("Not enough space or invalid size")
            return False

    def del_file(self, name_file):
        """delete file from disk if exist"""

        if name_file not in self.files:
            print("The file not exist")
            return False
        else:
            del self.files[name_file]
            return True

    def update_file(self, name_file, size_file):
        """update file if exist"""

        if name_file not in self.files:
            print("The file not exist")
            return False
        else:
            self.files[name_file] = size_file
            return True

    def __str__(self):
        return (f'The size of disk is {self.size}\n'
                f'The files in disk are {self.files}\n'
                f'#Free space: {self.free_space()}, #Used space: {self.used_space()}\n')


# == main ==
if __name__ == "__main__":

    disk1 = Hard_disk(100)
    print(disk1)

    disk1.add_file("movie", 20)
    print(disk1)

    disk1.update_file("movie", 30)
    print(disk1)

    disk1.del_file("movie")
    print(disk1)
