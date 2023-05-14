
# Defining a class to represent memory partitions
class Partition:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.size = end - start + 1
        self.is_allocated = False
        self.process_id = None

    def allocate(self, process_id):
        self.is_allocated = True
        self.process_id = process_id

    def deallocate(self):
        self.is_allocated = False
        self.process_id = None


# Defining a class to represent memory
class Memory:
    def __init__(self, partitions):
        self.partitions = partitions

    # Method to allocate memory to a process
    def allocate_memory(self, process_id, process_size):
        for partition in self.partitions:
            if partition.is_allocated == False and partition.size >= process_size:
                partition.allocate(process_id)
                return True
        return False

    # Method to deallocate memory from a process
    def deallocate_memory(self, process_id):
        for partition in self.partitions:
            if partition.process_id == process_id:
                partition.deallocate()

    # Method to display the memory status
    def display_memory(self):
        for partition in self.partitions:
            if partition.is_allocated:
                print("Partition start: {}, Partition end: {}, Process ID: {}".format(
                    partition.start, partition.end, partition.process_id))
            else:
                print("Partition start: {}, Partition end: {}, Free".format(
                    partition.start, partition.end))


# Creating memory partitions
partitions = [Partition(0, 9), Partition(10, 19), Partition(
    20, 29), Partition(30, 39), Partition(40, 59)]

# Creating memory object
memory = Memory(partitions)


if __name__ == "__main__":
    while True:
        print('''
Multiprogramming with variable number of tasks
Enter following options:
1. Memory allocation
2. Memory deallocation
3. Exit
''')
        choice = input("Enter the choice: ")
        if choice == "1":
            print("---Initiating Memory allocation---")
            program_name = input("Enter the Program Name: ")
            program_size = int(input("Enter size of the program: "))
            if memory.allocate_memory(program_name, program_size):
                print("Memory allocated successfully.")
            else:
                print("Not able to allocate memory.")

        elif choice == "2":
            print("----Initiating Memory Deallocation----")
            program_name = input("Enter the Program Name: ")
            memory.deallocate_memory(program_name)

        elif choice == "exit":
            break
        else:
            print("Enter a valid choice.")

        print("Current memory state: ")
        memory.display_memory()
