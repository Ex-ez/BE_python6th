def val(lst):
    print("Inside Function Before Append:", lst, id(lst))
    lst.append(4)
    print("Inside Function After Append:", lst, id(lst))


list = [1, 2, 3]
print("Before Calling Function:", list, id(list))
val(list)
print("After Calling Function:", list, id(list))
