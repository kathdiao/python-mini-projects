#   Arbitrary Arguments - *args
def find_max(*numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    for n in numbers:
        if n > max_num:
            max_num = n
    return max_num

print(find_max(4, 9, 6, 2, 11, 23, 1))


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



#   Arbitrary Arguments - **kwargs
def kwargs(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(f"{key}: {value}" )

kwargs("kath", age = 22, province= "zambales", hobby = "coding")



def args_kwargs(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

args_kwargs("User Info", "Aiah", "Fleur", age = 25, city = "Baguio")