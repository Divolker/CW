def mul_by_n(lst, n):
    print("Inputs: ", lst, n) # Check our inputs
    result = (x * n for x in lst)
    return list(result)
c=mul_by_n([9, 1], 4)
print(c)