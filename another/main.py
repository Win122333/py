from Student import Student


def get_unique_list_items(lst):
    return [lst[i] for i in range(len(lst)) if i + 1 >= len(lst) or lst[i + 1] != lst[i]]


def get_bool_list_of_saddle_points(mtrx):
    ans_list = [[False for _ in range(len(mtrx[0]))] for _ in range(len(mtrx))]
    for row in range(len(mtrx)):
        for column in range(len(mtrx[row])):
            ans_list[row][column] = (mtrx[row][column] == min(mtrx[row])
                                     and mtrx[row][column] == max([mtrx[i][column] for i in range(len(mtrx))]))
    return ans_list


def take_student(students, n):
    unpack_student_info = sorted(students, reverse=True)
    return unpack_student_info[:n]

def main():

    d = (i ** 2 for i in range(1, 6))
    print(9 in d, 4 in d)

    # with open('/another/input3.txt') as f:
    #     sts = [Student(*i.split(', ')) for i in f.readlines()]
    #
    #
    # answer = take_student(sts, 2)
    # for i in answer:
    #     print(i)

    # with open('/Users/win122333/PycharmProjects/pyMain/out3.txt') as f:
    #     for i in range(len(answer)):
    #         f.write(' '.join(map(str, answer[i])))
if __name__ == '__main__':
    main()
