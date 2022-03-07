import math
from decorators import *


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"


@debug
@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])


# waste_some_time(10)
# make_greeting("Balu", 34)

math.factorial = debug(math.factorial)


def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))


# print(approximate_e(5))


@slow_down
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)


# countdown(3)


@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"


def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)


randomly_greet("Alice")
randomly_greet("Alice")
