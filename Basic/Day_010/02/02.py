from art import logo
OPERATIONS_LIST = ["+", "-", "*", "/"]

def pick_first_number():
    number = float(input("What's the first number?\n"))
    return number

def pick_second_number():
    number = float(input("What's the next number?\n"))
    return number

def choose_operation():
    operation = input("+, -, *, /\nPick an operation: ")
    index_of_operation = OPERATIONS_LIST.index(operation)
    return index_of_operation

def calculate(n_0, operation, n_1):
    if operation == 0:
        return (n_0 + n_1)
    elif operation == 1:
        return (n_0 - n_1)
    elif operation == 2:
        return (n_0 * n_1)
    elif operation == 3:
        return (n_0 / n_1)

def keep_operating(result):
    n_0 = result
    operation = choose_operation()
    n_1 = pick_second_number()
    result = calculate(n_0, operation, n_1)
    print("{} {} {} = {}".format(n_0, OPERATIONS_LIST[operation], n_1, result))
    return result    

def main():
    keep_running = True
    while keep_running:
        want_to_keep_operating = True
        print(logo)
        n_0 = pick_first_number()
        operation = choose_operation()
        n_1 = pick_second_number()
        result = calculate(n_0, operation, n_1)
        print("{} {} {} = {}".format(n_0, OPERATIONS_LIST[operation], n_1, result))
        want_to_keep = input("Type 'y' to continue calculating with {}, or type 'n' to start a new calculation: ".format(result))
        if want_to_keep == "n":
            want_to_keep_operating = False
        while want_to_keep_operating:
            result = keep_operating(result)
            want_to_keep = input("Type 'y' to continue calculating with {}, or type 'n' to start a new calculation: ".format(result))
            if want_to_keep == "n":
                want_to_keep_operating = False
        want_to_keep_running = input("want to calculate something else?\nType 'yes' to continue or 'exit' to quit the aplication\n").lower()
        if keep_running == "yes":
            main()
        elif keep_running == "exit":
            keep_running = False
    print("Thanks for using!")

main()
