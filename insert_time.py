import random
import time

def insert_sort(array):
    for i in range(1, len(array)):
        curr = array[i]
        pos = i

        while pos > 0 and array[pos - 1] > curr:
            array[pos] = array[pos - 1]
            pos -= 1

        array[pos] = curr

def random_num_gen():
    new_num = input("Hi how many numbers would you like to generate? ")
    random_list = [random.randrange(0, 10001, 1) for i in range(int(new_num))]

    return random_list


def main():
    rand_num_list = random_num_gen()
    start = time.perf_counter()
    insert_sort(rand_num_list)
    elapsed = (time.perf_counter() - start)
    print("Size of n: ", len(rand_num_list))
    print("Elapsed Time: ", elapsed, "seconds")




if __name__ == "__main__":
    main()