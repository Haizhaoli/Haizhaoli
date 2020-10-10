import re
from yunsuan import formula_change, formula_result
from fractions import Fraction


def formula_answer(formula_list):
    for i, formula in enumerate(formula_list):
        formula_str = str(i + 1)
        formula_value = str(formula_result(formula_change(formula))) + '\n'
        if formula_value.find('/') > 0:
            num = formula_value.split('/')
            left = int(num[0])
            right = int(num[1])
            if left < right:
                answer = formula_str + ':' + formula_value
            else:
                first = left // right
                numerator = left % right
                formula_value = str(first) + "'" + str(Fraction(numerator, right)) +'\n'
                answer = formula_str + ':' + formula_value
        else:
            answer = formula_str + ':' + formula_value
        with open('Answer.txt', 'a+', encoding='utf-8') as file:
            file.write(answer)


def check(exercisefile, answerfile):
    right_num = 0
    wrong_num = 0
    right_list = []
    wrong_list = []
    exercise_result = []

    try:
        with open(exercisefile, 'r', encoding='utf-8') as file:
            for line in file:
                formula_str = re.findall(r'\d+: (.*) = \n', line)
                if formula_str:
                    formula = formula_str[0]
                else:
                    continue
                formula_value = str(formula_result(formula_change(formula)))
                exercise_result.append(formula_value)
    except IOError:
        print('请查看输入的路径是否正确')

    try:
        with open(answerfile, 'r', encoding='utf-8') as file:
            for i, line in enumerate(file):
                answer_str = re.findall(r'\d+: (.*) = \n', line)
                if answer_str:
                    answer = answer_str[0]
                else:
                    continue
                if answer == exercise_result[i]:
                    right_num += 1
                    right_list.append(i + 1)
                else:
                    wrong_num += 1
                    wrong_list.append(i + 1)
        with open('Grade.txt', 'w', encoding='utf-8') as file:
            right_str = 'Right:' + str(right_num) + ' ' + str(right_list) + '\n'
            wrong_str = 'Wrong:' + str(wrong_num) + ' ' + str(wrong_list)
            file.write(right_str)
            file.write(wrong_str)
    except IOError:
        print('请查看输入的路径是否正确')
