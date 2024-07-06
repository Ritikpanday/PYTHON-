def contains_even_number(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            print(f"List {lst} contains an even number.")
            break
        if i == len(lst)-1:
            print(f"List {lst} does not contain an even number.")



contains_even_number([1, 9, 8])
contains_even_number([1, 3, 5])
