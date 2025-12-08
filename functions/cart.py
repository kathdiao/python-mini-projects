#   Arbitrary Arguments - *args
def find_max(*numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

print(find_max(3, 9, 6, 2, 11, 23, 1))


def args_access(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

args_access("Babi", "Kiwi", "Coli")


def display(greeting, *names):
    for name in names:
        print(greeting, name)

display("Hello", "Tench", "Drei", "Kiel")