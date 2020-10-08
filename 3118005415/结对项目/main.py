# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 Double Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
import argparse

from creation import configuration, construction
from solution import formula_answer, check


def main():
    # 在下面的代码行中使用断点来调试脚本。
    parser = argparse.ArgumentParser(description="***** this is auto-generate-expression *****")
    parser.add_argument("-n", metavar="--number", dest="formula_num_arg", help="Generate a given number of expressions")
    parser.add_argument("-r", metavar="--range", dest="range_arg", help="Specify the range of operands")
    parser.add_argument("-e", metavar="--exercise file", dest="exercise_arg",
                        help="Given four arithmetic problem files")
    parser.add_argument("-a", metavar="--answer file", dest="answer_arg",
                        help="Given four arithmetic problem answer files")
    args = parser.parse_args()

    if args.formula_num_arg:
        if args.range_arg:
            config = configuration(formula_num=int(args.formula_num_arg), num_length=int(args.range_arg))
        else:
            config = configuration(formula_num=args.formula_num_arg)
        print('**** 程序正在生成满足要求的各项表达式 ****')
        building = construction()
        result_list = building.construct(config)
        building.formula_output(result_list)
        formula_answer(result_list)
        print('**** 所需题目已生成完毕 ****')

        if args.exercise_arg:
            if args.answer_arg:
                check(args.exercise_arg, args.answer_arg)
            else:
                print('请给出答案文件')
                exit(0)


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    main()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
