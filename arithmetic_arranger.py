def arithmetic_arranger(operation: list, ans: bool = False) -> object:
    split_prob = []
    operator = []
    prob_print_len = []
    prob_solution = []

    for _ in operation:
        if "+" in _:
            op_pair = _.split(" + ")
            op_pair_int: list = []
            split_prob.extend(op_pair)
            operator.append('+')
            for _ in range(len(op_pair)):
                if op_pair[_].isnumeric():
                    op_pair_int.append(int(op_pair[_]))
                else:
                    return "Error: Numbers must only contain digits."

            opera_len = 1
            for _ in op_pair:
                if opera_len < len(_):
                    opera_len = len(_)
            prob_print_len.append(opera_len + 2)
            prob_solution.append(sum(op_pair_int))

        elif "-" in _:
            op_pair = _.split(" - ")
            op_pair_int: list = []
            split_prob.extend(op_pair)
            operator.append('-')

            for _ in range(len(op_pair)):
                if op_pair[_].isnumeric():
                    op_pair_int.append(int(op_pair[_]))
                else:
                    return "Error: Numbers must only contain digits."

            opera_len = 1
            for _ in op_pair:
                if opera_len < len(_):
                    opera_len = len(_)
            prob_print_len.append(opera_len + 2)
            prob_solution.append(op_pair_int[0] - op_pair_int[1])
        else:
            return "Error: Operator must be '+' or '-'."

    problems_quantity = len(operator)
    if problems_quantity > 5:
        return "Error: Too many problems."
    else:

        print_line1 = ""
        print_line2 = ""
        print_line3 = ""
        print_line4 = ""
        n = 0
        for _ in range(len(prob_print_len)):

            if prob_print_len[_] > 6:
                return "Error: Numbers cannot be more than four digits."

            else:
                if _ == (len(prob_print_len) - 1):
                    number1 = right_align(prob_print_len[_], split_prob[n])
                    print_line1 = print_line1 + number1 + "\n"
                    number2 = right_align(prob_print_len[_], split_prob[n + 1], 1)
                    print_line2 = print_line2 + operator[_] + number2 + "\n"
                    print_line3 += "-" * prob_print_len[_]
                    number3 = right_align(prob_print_len[_], str(prob_solution[_]))
                    print_line4 = print_line4 + number3

                else:
                    number1 = right_align(prob_print_len[_], split_prob[n])
                    print_line1 = print_line1 + number1 + "    "
                    number2 = right_align(prob_print_len[_], split_prob[n + 1], 1)
                    print_line2 = print_line2 + operator[_] + number2 + "    "
                    print_line3 += "-" * prob_print_len[_] + "    "
                    number3 = right_align(prob_print_len[_], str(prob_solution[_]))
                    print_line4 = print_line4 + number3 + "    "
                n += 2

        if ans:
            arranged_problems = print_line1 + print_line2 + print_line3 + "\n" + print_line4
            return arranged_problems

        else:
            arranged_problems = print_line1 + print_line2 + print_line3
            return arranged_problems


def right_align(number_available_characters: int, characters_to_show: str, displacement: int = 0):
    number_blank_spaces = number_available_characters - (len(characters_to_show) + displacement)
    right_aligned_text = (" " * number_blank_spaces) + characters_to_show
    return right_aligned_text
