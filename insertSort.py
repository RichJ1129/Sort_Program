def insert_sort(array):
    for i in range(1, len(array)):
        curr = array[i]
        pos = i

        while pos > 0 and array[pos - 1] > curr:
            array[pos] = array[pos - 1]
            pos -= 1

        array[pos] = curr

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
    data_map = file_handling(data_content)

    for key in data_map:
        new_list = list(data_map[key])
        new_list = [int(i) for i in new_list]
        insert_sort(new_list)
        printList(new_list)


if __name__ == "__main__":
    main()








