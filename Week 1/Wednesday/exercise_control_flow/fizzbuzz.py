"""
Task 2: FizzBuzz Extended
Prints numbers 1 through n with Fizz/Buzz/Boom rules.
"""


def fizzbuzz(n):
    for i in range(1, n + 1):
        div3 = i % 3 == 0
        div5 = i % 5 == 0
        div7 = i % 7 == 0

        if div3 and div5 and div7:
            print("FizzBuzzBoom")
        elif div3 and div5:
            print("FizzBuzz")
        elif div3 and div7:
            print("FizzBoom")
        elif div5 and div7:
            print("BuzzBoom")
        elif div3:
            print("Fizz")
        elif div5:
            print("Buzz")
        elif div7:
            print("Boom")
        else:
            print(i)


if __name__ == "__main__":
    fizzbuzz(105)
