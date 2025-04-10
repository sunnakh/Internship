# o  1 dan 20 gacha bo‘lgan sonlar ro‘yxatini yaratib, faqat juftlarini lambda va list comprehension yordamida ajrating.

numbers =  list(range(1, 21))
oddnumbers = list(filter(lambda x: x % 2 != 0, numbers))
evenumbers = list(filter(lambda x: x %  2 == 0, numbers))\

print(oddnumbers)
print(evenumbers)