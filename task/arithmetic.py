# write your code here
import random


def creation_of_simple_equation():
    equation = ''
    operators = ['+', '-', '*']
    random.seed()

    equation += str(random.randint(2, 9))
    equation += ' '
    equation += random.choice(operators)
    equation += ' '
    equation += str(random.randint(2, 9))

    return equation


def creation_of_harder_equation():
    return str(random.randint(11, 29))


def harder_calculator(equation):
    return int(equation) ** 2


def simple_calculator(equation):
    first_part = 0
    second_part = 0
    symbol = ''
    answer = 0

    for i in range(len(equation)):
        if equation[i] == '+' or equation[i] == '-' or equation[i] == '*':
            first_part = int(equation[:i])
            second_part = int(equation[i + 1:])
            symbol = equation[i]
            break

    if symbol == '+':
        answer = first_part + second_part
    elif symbol == '-':
        answer = first_part - second_part
    elif symbol == '*':
        answer = first_part * second_part

    return answer


def main():
    actual_mark = 0
    print('Which level do you want? Enter a number:\n'
          '1 - simple operations with numbers 2-9\n'
          '2 - integral squares of 11-29')

    while True:
        try:
            level = int(input())
            if level > 2:
                assert ValueError
        except ValueError:
            print("Incorrect format.")
        else:
            break

    for i in range(5):
        if level == 1:
            equation_to_solve = creation_of_simple_equation()
            level_description = 'simple operations with numbers 2-9'
        else:
            equation_to_solve = creation_of_harder_equation()
            level_description = 'integral squares of 11-29'
        print(equation_to_solve)
        while True:
            try:
                answer = int(input())
            except ValueError:
                print("Incorrect format.")
            else:
                if (level == 1 and answer == simple_calculator(equation_to_solve)) or \
                        (level == 2 and answer == harder_calculator(equation_to_solve)):
                    print('Right!')
                    actual_mark += 1
                else:
                    print('Wrong!')
                break
    print(f"Your mark is {actual_mark}/5.")
    print('Would you like to save your result to the file? Enter yes or no.')
    answer_to_save = input().lower()
    if answer_to_save == 'yes' or answer_to_save == 'y':
        print('What is your name?')
        name = input()
        with open('results.txt', 'a') as file:
            file.write(f'{name}: {actual_mark}/5 in level {level} ({level_description}).\n')
            file.close()
        print('The results are saved in "results.txt".')


if __name__ == '__main__':
    main()
