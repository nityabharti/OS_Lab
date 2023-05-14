
from collections import deque


def print_q(queue):
    print("Current Queue:", end=" ")
    for val in queue:
        print(val, end=" ")
    print()


def lru(pages, capacity):
    page_faults = 0
    page_frames = deque(maxlen=capacity)
    page_dict = {}

    for page in pages:
        if page not in page_dict:
            page_faults += 1
            if len(page_frames) == page_frames.maxlen:
                # removing from the frame and also from dictionary
                val = page_frames.popleft()
                del page_dict[val]
                print(f"Queue is full. Removing page {val}")
            page_dict[page] = True
            page_frames.append(page)
            print(f"Adding page {page} to queue.")
        else:
            print(f"Page {page} already exsits, marking it as recent.")
            # Removing and adding the page again to mark it as recently accessed.
            page_frames.remove(page)
            page_frames.append(page)

        print("Current Queue: ")
        print_q(page_frames)

    return page_faults


if __name__ == "__main__":
    frames = int(input("Enter numeber of frames: "))
    pages = [int(x)
             for x in input("Enter sequence of page access: ").split(" ")]

    page_faults = lru(pages, frames)
    print("Page Faults: ", page_faults)
