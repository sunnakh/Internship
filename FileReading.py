# 2.  Fayl o‘qish va yozish:
# o  Keyin fayldan matnni o‘qing va ekranga chiqaring.

with open('data.txt', 'r') as file:
    content = file.read()
    print(content)