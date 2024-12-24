# # Hackerrank 1
#
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a+b)
#     print(a-b)
#     print(a*b)
"""---------------------------------------------------"""
# # Hackerrank 2
#
# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     max_score = second_score = 0
#     for i in arr:
#         if i > max_score :
#             second_score = max_score
#             max_score = i
#         elif i > second_score and i < max_score :
#             second_score = i
#     print(second_score)
"""---------------------------------------------------"""
# # Hackerrank 3
#
# if __name__ == '__main__':
#     n = int(input())
#     str_list = ""
#     for i in range(1,n+1):
#         str_list += str(i)
#     print(str_list)
"""---------------------------------------------------"""
# # Hackerrank4
#
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     not_toplam = 0
#     for i in student_marks[query_name]:
#         not_toplam += i
#     ortalama = f"{(not_toplam/len(student_marks[query_name])):.2f}"
#     print(ortalama)
"""---------------------------------------------------"""
regex_integer_in_range = r"_________"  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"_________"  # Do not delete 'r'.

import re

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

number_examined_list = list()
for i in range(len(regex_alternating_repetitive_digit_pair) - 2):
    if (regex_alternating_repetitive_digit_pair[i] == regex_alternating_repetitive_digit_pair[i + 2] and
            regex_alternating_repetitive_digit_pair[i] != regex_alternating_repetitive_digit_pair[i + 1]):
        number_examined_list.append[regex_alternating_repetitive_digit_pair[i]]
print(len(number_examined_list) > 0)