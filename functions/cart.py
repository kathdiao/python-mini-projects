#   Arbitrary Arguments - *args
def find_max(*numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

print(find_max(3, 7, 2, 9, 1))


def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All arguments:", args)

my_function("Babi", "Kiwi", "Coli")


def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "Tench", "Drei", "Kiel")