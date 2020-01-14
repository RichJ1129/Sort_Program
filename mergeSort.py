def merge_sort(array):
    if len(array) > 1:
        mid_num = len(array) // 2 #Find the middle of the list "//" used so that integer is returned
        left = array[:mid_num] # Gets the elements to the left of middle number
        right = array[mid_num:] # Holds elements to the right of the middle number including middle number

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
            array[k]  = left[i]
            i += 1
            k += 1

        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


def file_handling(content):
    data_map = {}
    line_num = 0
    line_list = []
    new_num = ""

    for i in range(len(content)):
        if content[i] == " ":
            line_list.append(new_num)
            new_num = ""
        elif content[i] == "\n":
            line_list.append(new_num)
            new_num = ""
            line_num += 1
            key = line_num
            data_map[key] = line_list[:]
            line_list.clear()
        elif i == len(content) - 1:
            new_num += content[i]
            line_list.append(new_num)
            line_num += 1
            key = line_num
            data_map[key] = line_list[:]
            line_list.clear()
        else:
            new_num += content[i]

    return data_map

def main():
    data_file = open("data.txt")
    data_content = data_file.read()
    file_handling(data_content)

    array = [10, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    merge_sort(array)
    printList(array)


if __name__ == "__main__":
    main()
