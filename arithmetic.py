# write your code here
import random


def first_level(n):
    for i in range(5):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        op_list = ["+", "-", "*"]
        op = random.choice(op_list)
        math = eval(str(a) + op + str(b))
        str_math = str(a) + " " + op + " " + str(b)
        print(str_math)
        while True:
            try:
                answer = int(input())
                break
            except ValueError:
                print("Incorrect format.")
        if math == answer:
            print("Right!")
            n += 1
        else:
            print("Wrong!")
    return n


def second_level(n):
    for i in range(5):
        sqr = random.randint(11, 29)
        print(sqr)
        math = sqr ** 2
        while True:
            try:
                answer = int(input())
                break
            except ValueError:
                print("Incorrect format.")
        if math == answer:
            print("Right!")
            n += 1
        else:
            print("Wrong!")
    return n


yes_variants = ["yes", "YES", "y", "Yes", "Y"]
mark = 0
print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")
while True:
    try:
        level_chose = int(input())
        if level_chose == 1:
            level_description = '(simple operations with numbers 2-9)'
            mark = first_level(mark)
            break
        elif level_chose == 2:
            level_description = '(integral squares of 11-29)'
            mark = second_level(mark)
            break
        else:
            print("Incorrect format.")
    except ValueError:
        print("Incorrect format.")
print(f"Your mark is {mark}/5. Would you like to save the result? Enter yes or no.")
while True:
    save_chose = input()
    if save_chose in yes_variants:
        with open("results.txt", 'a', encoding='utf-8') as results_file:
            print("What is your name?")
            name = input()
            results_file.write(f"{name}: {mark}/5 in level {level_chose} {level_description}./n")
            print('The results are saved in "results.txt".')
            results_file.close()
        break
    else:
        break
