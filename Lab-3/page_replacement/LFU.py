
from collections import defaultdict


def lfu(page_reference, frame_size):

    # initialize the page frames and page faults count
    page_frames = []
    page_faults = 0

    # initialize the dictionary to track the frequency of each page
    page_frequency = defaultdict(int)

    # iterate through the page reference sequence
    for page in page_reference:
        # check if the page is already in the page frames
        if page in page_frames:
            # increment the frequency count of the page
            page_frequency[page] += 1
            print(f"Page {page} already exits.")
            continue

        # if the page is not in the page frames, we need to replace a page
        page_faults += 1

        # if there is still room in the page frames, just add the page
        if len(page_frames) < frame_size:
            page_frames.append(page)
        else:
            # if all page frames are occupied, find the least frequently used page
            least_frequent_page = page_frames[0]
            for frame in page_frames:
                if page_frequency[frame] < page_frequency[least_frequent_page]:
                    least_frequent_page = frame

            # replace the least frequently used page with the new page
            page_frames.remove(least_frequent_page)
            print(f"Removed Least Frequently Used Page {least_frequent_page}")
            page_frames.append(page)
        print(f"Added page {page}")

        # increment the frequency count of the new page
        page_frequency[page] += 1
        print("Current Queue: ", page_frames)

    return page_faults


if __name__ == "__main__":
    frame_size = int(input("Enter numeber of frames: "))
    page_reference = [int(x) for x in input(
        "Enter sequence of page access: ").split(" ")]

    page_faults = lfu(page_reference, frame_size)

    # print the page faults count
    print("Total page faults:", page_faults)
