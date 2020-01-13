def merge_sort(array):
    data_file = open("data.txt")
    data_content = data_file.read()

    if len(array) > 1:
        mid_num = len(array) // 2 #Find the middle of the list "//" used so that integer is returned
        left = array[:mid_num] # Gets the elements to the left of middle number
        right = array[mid_num:] # Holds elements to the right of the middle number including middle number


def main():
    array = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

    merge_sort()


if __name__ == "__main__":
    main()
