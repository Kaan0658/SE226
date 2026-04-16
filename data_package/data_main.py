from data_package import (
    remove_duplicates,
    strip_whitespaces,
    calculate_mean,
    find_maximum,
    find_minimum
)


data = input("Enter numbers separated by commas: ")


data_list = data.split(",")


cleaned_strings = strip_whitespaces(data_list)

numbers = [int(x) for x in cleaned_strings]

numbers = remove_duplicates(numbers)

mean_val = calculate_mean(numbers)
max_val = find_maximum(numbers)
min_val = find_minimum(numbers)


print("Cleaned Data:", numbers)
print("Mean:", mean_val)
print("Max:", max_val)
print("Min:", min_val)