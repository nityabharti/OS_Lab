

class FS:
    def __init__(self, name, isDirectory):
        self.name = name
        self.isDirectory = isDirectory


class Directory(FS):
    def __init__(self, name, parent=None):
        super().__init__(name, isDirectory=True)
        self.parent = parent
        self.children = {}

    def create_file(self, file_name):
        if not self.children.get(file_name):
            self.children[file_name] = File(file_name)
            print(f"{file_name} has been created.")
        else:
            print(f"A file with the file name {file_name} already exits.")

    def get_child(self, file_name):
        if not self.children.get(file_name):
            print(f"File with the name {file_name} doesn't exist.")
            return None
        return self.children[file_name]

    def rm_child(self, file_name):
        if not self.children.get(file_name):
            print(f"File with the name {file_name} doesn't exist.")
            return None
        del self.children[file_name]
        print(f"{file_name} has been deleted.")

    def ls(self):
        for key in self.children:
            print(key)


class File(FS):
    def __init__(self, name):
        super().__init__(name, isDirectory=False)
        self.extension = name.split(".")[-1]
        self.data = ""

    def write(self, data, mode='w'):
        if mode == 'w':
            self.data = data
        elif mode == 'a':
            self.data += data

    def __repr__(self):
        return self.data


if __name__ == "__main__":
    rd = Directory("Root_Directory")
    while True:
        user_statement = input(">> ").split(" ")
        cmd = user_statement[0]

        if cmd == "create":
            rd.create_file(user_statement[1])

        elif cmd == "rm":
            rd.rm_child(user_statement[1])

        elif cmd == "write":
            file = rd.get_child(user_statement[1])
            if file:
                file.write(user_statement[2])
        elif cmd == "list":
            rd.ls()
        elif cmd == "show":
            file = rd.get_child(user_statement[1])
            print(file)
        elif cmd == "exit":
            break
        else:
            print('''
Available commands are:

create [file name] - to create a file.
list - to list the files in root directory.
rm [file name] - to remove an exiting command.
show [file name] - to display the contents of the file.
wirte [file name] [content] - to write the content into the file.
exit - to exit out of the program
''')
