starting_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_inefficient_list = []

for i in starting_numbers:
    my_inefficient_list.append(i + 10)

print(my_inefficient_list)

my_efficient_list = [2*my_inefficient_list[i]-(i+1) for i in range(len(starting_numbers))]
print(my_efficient_list)
