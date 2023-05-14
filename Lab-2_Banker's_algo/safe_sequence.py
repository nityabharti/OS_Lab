import numpy as np
result = []

def safe_sequence_all(needed, allocated, available_resources, num_process, num_resources, safe_sequence=[], finished=set()):

    if len(finished) == num_process:
        result.append([x for x in safe_sequence])

    for i in range(num_process):
        if not i in finished and all(needed[i] <= available_resources):
            finished.add(i)
            available_resources += allocated[i]
            safe_sequence.append(f"P{i+1}")

            safe_sequence_all(needed, allocated, available_resources,
                              num_process, num_resources, safe_sequence, finished)

            finished.remove(i)
            available_resources -= allocated[i]
            safe_sequence.pop()


def resource_request(needed, allocated, requested, available_resources, process_num):
    if any(requested > needed[process_num]):
        raise Exception("Invalid Request: requested for more than needed.")

    if any(requested > available_resources):
        raise Exception("Invalid Request: requested for more than available.")

    # else Request granted
    available_resources -= requested
    allocated[process_num] += requested
    needed[process_num] -= requested

    return True

if __name__ == "__main__":
    num_process = int(input("Enter number of processess: "))
    num_resources = int(input("Enter number of resources: "))
    max_needed = np.zeros((num_process, num_resources), dtype='int32')
    allocated = np.zeros((num_process, num_resources), dtype='int32')

    for i in range(num_process):
        for j in range(num_resources):
            max_needed[i, j] = int(
                input(f"Enter Max Needed of R{j+1} for  P{i+1} : "))

    for i in range(num_process):
        for j in range(num_resources):
            allocated[i, j] = int(
                input(f"Enter R{j+1} allocated for  P{i+1} : "))

    available_resources = []

    for i in range(num_resources):
        available_resources.append(
            int(input(f"Enter the available resources of R{i+1}: ")))

    available_resources = np.array(available_resources, dtype='int32')
    needed = max_needed - allocated
    print('''
Options:
Enter 1 for making resource request
Enter 0 to skip
    ''')
    choice = int(input(">>> "))
    if choice == 1:
        request = []
        process_num = int(input("Which process is requesting: "))
        for i in range(num_resources):
            request.append(
                int(input(f"Enter number of resources request for R{i+1}: ")))
        request = np.array(request, dtype='int32')
        resource_request(needed, allocated, request,
                         available_resources, process_num)

    safe_sequence_all(needed, allocated, available_resources,
                      num_process, num_resources)
    if result:
        print("The All possible safe sequences are: ")
        for sequence in result:
            print(sequence)
    else:
        print("Not a safe state")
