import random
import string


def rand(n):
    lst = [random.choice(string.ascii_letters + string.digits) for n1 in range(n)]
    str = "".join(lst)
    print(str)


rand(16)
