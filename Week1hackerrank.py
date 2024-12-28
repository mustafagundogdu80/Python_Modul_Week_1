# Hackerrank 1

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
"""---------------------------------------------------"""
# Hackerrank 2

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max_score = second_score = -101
    for i in arr:
        if i > max_score :
            second_score = max_score
            max_score = i
        elif i > second_score and i < max_score :
            second_score = i
    print(second_score)
"""---------------------------------------------------"""
# Hackerrank 3

if __name__ == '__main__':
    n = int(input())
    str_list = ""
    for i in range(1,n+1):
        str_list += str(i)
    print(str_list)
"""---------------------------------------------------"""
# Hackerrank4

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    # The variable in which the sum of the notes is kept
    scores_sum = 0

    for i in student_marks[query_name]:
        scores_sum += i
    # Variable whose average values will be printed
    avarage_str = f"Avarage = {(scores_sum/len(student_marks[query_name])):.2f}"
    print(avarage_str)
"""---------------------------------------------------"""
