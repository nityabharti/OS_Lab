

class FS:
    def __init__(self, name, isDirectory):
        self.name = name
        self.isDirectory = isDirectory


class Directory(FS):
    def __init__(self, name, parent=None):
        super().__init__(name, isDirectory=True)
        self.parent = parent
        self.children = {}

    def current_working_dir(self):
        if self.parent:
            return self.parent.current_working_dir() + '/' + self.name
        else:
            return self.name

    def change_directory(self, dir_name):

        if dir_name == "..":
            if not self.parent:
                return self
            return self.parent
        elif dir_name == ".":
            return self
        elif dir_name in self.children:
            return self.children[dir_name]
        else:
            print(f"Directory {dir_name} doesn't exist.")

    def create_dir(self, dir_name):
        if not self.children.get(dir_name):
            self.children[dir_name] = Directory(dir_name, parent=self)
            print(f"{dir_name} directory has been created.")
        else:
            print(f"A directory with the name {dir_name} already exists")

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

    def link_file(self, file):
        if not self.children.get(file.name):
            self.children[file.name] = file
            file.link_count += 1
            print(f"{file.name} has been linked.")
        else:
            print(f"A file with the file name {file.name} already exits.")


class File(FS):
    def __init__(self, name):
        super().__init__(name, isDirectory=False)
        self.extension = name.split(".")[-1]
        self.data = ""
        self.link_count = 1

    def write(self, data, mode='w'):
        if mode == 'w':
            self.data = data
        elif mode == 'a':
            self.data += data

    def __repr__(self):
        return self.data


class System:
    users = []
    current_user = None

    def __init__(self):

        self.root_dir = Directory("root")
        self.current_dir = self.root_dir

        self.init()

    def init(self):
        while not self.current_user:
            prompt = '''
No user logged in right now.

Use:
login - to login into the System
adduser - to create new user
'''
            print(prompt)
            cmd = input(">>> ").strip()
            if cmd == "login":
                self.login()
            elif cmd == "adduser":
                self.adduser()

    def verifyUser(self, username, password):
        found_user = False
        # print(self.users)
        for user in self.users:
            if user['username'] == username:
                found_user = True
                if user['password'] == password:
                    print(f"Successfully logged in as {username}")
                    self.current_user = username
                    self.root_dir.create_dir(username)
                    self.current_dir = self.root_dir.children[username]
                    return True
                else:
                    print("Incorrect password.")
                    return False
        if not found_user:
            print("User not found. Try creating a new user using \'adduser\' command")
        return False

    def login(self):
        username = input("username: ")
        password = input("password: ")

        return self.verifyUser(username, password)

    def adduser(self):
        username = input("username for new user: ").strip()
        password = input("password for new user: ").strip()

        self.users.append({'username': username, 'password': password})

        return self.verifyUser(username, password)

    def logout(self):
        print(f"{self.current_user} has logged out successfully.")
        self.current_user = None

    def change_directory(self, dir_name):
        self.current_dir = self.current_dir.change_directory(dir_name)

    def link(self, file_path):
        path = file_path.split("/")
        temp_dir = self.root_dir
        for dir in path[2:-1]:
            if dir not in temp_dir.children:
                print("Invalid path.")
                return False
            temp_dir = temp_dir.children[dir]
        file_name = path[-1]
        if file_name not in temp_dir.children:
            print("File doesn't exist.")
            return False
        self.current_dir.link_file(temp_dir.children[file_name])
        return True
