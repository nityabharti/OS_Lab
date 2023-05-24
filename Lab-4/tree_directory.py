from base import System


if __name__ == "__main__":
    prompt = '''
Available commands are:

touch [file name] - to create a file.
mkdir [directory name] - to create directory
ls - to list the files in root directory.
rm [file name] - to remove an exiting command.
show [file name] - to display the contents of the file.
wirte [file name] [content] - to write the content into the file.
pwd - to check present working directory
cd [directory] - to change directory
help - displays help information
logout - to exit as current user
exit - to exit out of the program
'''

    sys = System()

    while True:
        current_dir = sys.current_dir
        user_statement = input(
            f"${sys.current_user}-{current_dir.current_working_dir()}# ").split(" ")
        cmd = user_statement[0]

        if cmd == "touch":
            current_dir.create_file(user_statement[1])

        elif cmd == "rm":
            current_dir.rm_child(user_statement[1])

        elif cmd == "write":
            file = current_dir.get_child(user_statement[1])
            if file:
                file.write(user_statement[2])
        elif cmd == "ls":
            current_dir.ls()
        elif cmd == "show":
            file = current_dir.get_child(user_statement[1])
            print(file)
        elif cmd == "exit":
            break
        elif cmd == "pwd":
            print(current_dir.current_working_dir())
        elif cmd == "cd":
            try:
                selected_dir = user_statement[1].strip()
            except:
                selected_dir = '.'
            sys.change_directory(selected_dir)

        elif cmd == "mkdir":
            current_dir.create_dir(user_statement[1].strip())
        elif cmd == "logout":
            sys.logout()
            sys.init()
        elif cmd == "help":
            print(prompt)
        else:
            print(prompt)
