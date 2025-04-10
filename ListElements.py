# 4.  List va Tuple ishlatish:
# o  Berilgan listdagi eng katta va eng kichik elementlarni topadigan funksiya yozing


def find_largest_and_smallest_in_list(lst):
    if not lst:
        return "List is empty"
    
    largest = max(lst)
    smallest = min(lst)
    
    return f"Largest: {largest}, Smallest: {smallest}"


my_list = [3, 5, 7, 2, 8, 1]
result = find_largest_and_smallest_in_list(my_list)
print(result)
