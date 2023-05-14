
from collections import deque

def print_q(queue):
    print("Current Queue:", end=" ")
    for val in queue:
        print(val, end=" ")
    print()


def fifo(pages, frames):
    page_faults = 0
    queue = deque()  # Queue for storing pages
    for page in pages:
        if page not in queue:
            if len(queue) == frames:  # queue is full
                val = queue.popleft()
                print(f"Queue is full, removing {val}")
            queue.append(page)
            print(f"Adding {page} to queue.")
            # counting number of page faults
            page_faults += 1
        else:
            print(f"Page {page} already in the queue.")

        print_q(queue)

    return page_faults


if __name__ == "__main__":
    frames = int(input("Enter numeber of frames: "))
    pages = [int(x)
             for x in input("Enter sequence of page access: ").split(" ")]
    page_faults = fifo(pages, frames)
    print("Page Faults:", page_faults)

    
        