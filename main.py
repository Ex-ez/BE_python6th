def val(x):
    print("Inside :", x, id(x))
    x += 1
    print("Inside After:", x, id(x))

print("====")
x = 10
print("Before Calling:", x, id(x))
val(x)
print("After Calling: ", x, id(x))