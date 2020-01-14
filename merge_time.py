import random
import time

def merge_sort(array):
    if len(array) > 1:
        mid_num = len(array) // 2  # Find the middle of the list "//" used so that integer is returned
        left = array[:mid_num]  # Gets the elements to the left of middle number
        right = array[mid_num:]  # Holds elements to the right of the middle number including middle number

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1


def random_num_gen():
    new_num = input("Hi how many numbers would you like to generate? ")
    random_list = [random.randrange(0, 10001, 1) for i in range(int(new_num))]

    return random_list


def main():
    rand_num_list = random_num_gen()
    start = time.perf_counter()
    merge_sort(rand_num_list)
    elapsed = (time.perf_counter() - start)
    print("Size of n: ", len(rand_num_list))
    print("Elapsed Time: ", elapsed, " seconds")

if __name__ == "__main__":
    main()
