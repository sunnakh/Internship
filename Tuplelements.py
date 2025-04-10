# 4.  List va Tuple ishlatish:
# o  Berilgan listdagi eng katta va eng kichik elementlarni topadigan funksiya yozing

def find_largest_and_smallest_in_tuple(tpl):
    if not tpl:
        return "Tuple is empty"
    
    largest = max(tpl)
    smallest = min(tpl)
    
    return f"Largest: {largest}, Smallest: {smallest}"

my_tuple = (3, 5, 7, 2, 8, 1)
result = find_largest_and_smallest_in_tuple(my_tuple)
print(result)
