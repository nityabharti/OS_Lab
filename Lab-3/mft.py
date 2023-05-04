

partition_size = int(input("Enter the Partition Size: "))  # size of each partition

# number of partitions in memory
num_partitions = int(input("Enter Number of partitions in memory: "))
memory = [None] * num_partitions  # initialize memory

# function to allocate memory for a process


def allocate(process_name, num_partitions_needed):
    # check if there are enough free partitions
    if memory.count(None) < num_partitions_needed:
        print(f"Not enough free memory partitions for process {process_name}")
        return
    # find the first set of contiguous free partitions
    start_index = memory.index(None)
    end_index = start_index + num_partitions_needed
    # allocate memory for the process
    for i in range(start_index, end_index):
        memory[i] = process_name
    print(
        f"Allocated {num_partitions_needed} partitions for process {process_name} at {start_index}")

    return start_index

# function to deallocate memory for a process


def deallocate(process_name):
    # find the partitions allocated to the process
    allocated_partitions = [
        i for i, p in enumerate(memory) if p == process_name]

    if len(allocated_partitions) == 0:
        print(f"There are no processes with the {program_name}")

    # deallocate the partitions
    for i in allocated_partitions:
        memory[i] = None
    print(f"Deallocated partitions for process {process_name}")


if __name__ == "__main__":
    while True:
        print('''
Multiprogramming with fixed number of tasks
Enter following options:
1. Memory allocation
2. Memory deallocation
3. Exit
''')
        choice = int(input("Enter the choice: "))
        if choice == 1:
            print("---Initiating Memory allocation---")
            program_name = input("Enter the Program Name: ")
            partitions_required = int(
                input("Enter number of partitions required: "))
            allocate(program_name, partitions_required)

        elif choice == 2:
            print("----Initiating Memory Deallocation----")
            program_name = input("Enter the Program Name: ")
            deallocate(program_name)

        elif choice == "exit":
            break
        else:
            print("Enter a valid choice.")

        print("Current memory state:  n", memory)
