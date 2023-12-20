# Exercise 2:

numbers = [16, 2, 48, 77, 5]

for i in range(len(numbers)):
    if i == len(numbers) - 1:
        print(numbers[i] + numbers[0])
    else:
        print(numbers[i] + numbers[i + 1])



# another example:


# Create a list of five integers.
integer_list = [10, 20, 30, 40, 50]

# Use a for loop to print the sum of each item with the next item in the list,
# or with the first item if it's the last item in the list.
print("Sum of each item with the next item:")
for i in range(len(integer_list)):
    current_item = integer_list[i]
    next_item = integer_list[(i + 1) % len(integer_list)]  # Use modulo to wrap around for the last item
    sum_result = current_item + next_item
    print("Sum of {} and {}: {}".format(current_item, next_item, sum_result))
