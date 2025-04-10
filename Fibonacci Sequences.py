
# 3.  Fibonacci sonlari:
# o  n sonini foydalanuvchidan so‘rab, n-gacha bo‘lgan Fibonacci sonlarini chiqaradigan funksiya yozing.


def fibonacci(number):
    fib_sequence = [0, 1]
    while len(fib_sequence) < number:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:number]
number = int(input("Enter a number to gget Fibonacci sequence: "))
print(fibonacci(number))
