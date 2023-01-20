from collections import Counter
import random

bincom_shirt = ['GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'BLUE', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE',
                'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'ARSH', 'BROWN', 'GREEN', 'BROWN',
                'BLUE', 'BLUE', 'BLEW', 'PINK', 'PINK', 'ORANGE', 'ORANGE', 'RED', 'WHITE', 'BLUE', 'WHITE', 'WHITE',
                'BLUE', 'BLUE', 'BLUE', 'GREEN', 'YELLOW', 'GREEN', 'BROWN', 'BLUE', 'PINK', 'RED', 'YELLOW', 'ORANGE',
                'RED', 'ORANGE', 'RED', 'BLUE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'WHITE', 'WHITE', 'BLUE', 'BLUE',
                'GREEN', 'WHITE', 'BLUE', 'BROWN', 'PINK', 'YELLOW', 'ORANGE', 'CREAM', 'ORANGE', 'RED', 'WHITE',
                'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE', 'GREEN', 'GREEN', 'WHITE', 'GREEN', 'BROWN', 'BLUE', 'BLUE',
                'BLACK', 'WHITE', 'ORANGE', 'ORANGE', 'RED', 'RED', 'WHITE', 'BLUE', 'WHITE', 'BLUE', 'BLUE', 'BLUE',
                'WHITE']


def group_colors(colors):
    # Use the Counter class to group the colors
    grouped_colors = Counter(colors)

    # Return the grouped colors as a dictionary
    return dict(grouped_colors)


grouped = group_colors(bincom_shirt)


def mean_color_values(d):
    value_sum = 0
    value_count = 0

    # Iterate through the dictionary and add the values to the sum and increment the count
    for key, value in d.items():
        value_sum += value
        value_count += 1

    # Calculate the mean value by dividing the sum by the count
    mean_value = value_sum / value_count

    # Iterate through the dictionary again to find the key that holds the mean value
    for key, value in d.items():
        if value == round(mean_value):
            return key
    return None


def most_worn(dit):
    max_key = max(dit, key=dit.get)
    return max_key


def median_color(med_dit):
    sorted_dict = dict(sorted(med_dit.items(), key=lambda x: x[1]))

    # Get the keys of the sorted dictionary
    keys = list(sorted_dict.keys())

    # Get the length of the keys
    length = len(keys)

    # Check if the length of the keys is even or odd
    if length % 2 == 0:
        # If even, get the middle two keys
        middle1 = keys[length // 2 - 1]
        middle2 = keys[length // 2]
        # Calculate the average of the values
        median = (sorted_dict[middle1] + sorted_dict[middle2]) / 2
    else:
        # If odd, get the middle key
        middle = keys[length // 2]
        median = sorted_dict[middle]
    for key, value in med_dit.items():
        if value == round(median):
            return key,
    return None


# recursive searching algorithm to search for a number entered by user in a list of numbers

def search_recursive(numb, targ, start, end):
    # Base case: if start index is greater than end index, the target is not in the list
    if start > end:
        return -1

    # Get the middle index
    middle = (start + end) // 2

    # Check if the middle element is the target
    if numb[middle] == targ:
        return middle

    # If the target is less than the middle element, search the left half of the list
    elif targ < numb[middle]:
        return search_recursive(numb, targ, start, middle - 1)

    # If the target is greater than the middle element, search the right half of the list
    else:
        return search_recursive(numb, targ, middle + 1, end)


# testing the algorithm
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
tgt = int(input("Enter a number to search for: "))

result = search_recursive(numbers, tgt, 0, len(numbers) - 1)

if result != -1:
    print("The number", tgt, "is at index", result)
else:
    print("The number", tgt, "is not in the list")

# Write a program that generates random 4 digits number of 0s and 1s and convert the generated number to base 10.

# Generate a random 4-digit number of 0s and 1s
binary_number = ''.join(random.choices(['0', '1'], k=4))

# Convert the binary number to base 10
decimal_number = int(binary_number, 2)

print("Random 4-digit binary number:", binary_number)
print("Decimal equivalent:", decimal_number)

# Write a program to sum the first 50 fibonacci sequence.

# Initialize the first two Fibonacci numbers
fib1 = 0
fib2 = 1

# Initialize the sum
sum = 0

# Initialize the counter
count = 0

while count < 50:
    # Add the current Fibonacci number to the sum
    sum += fib2

    # Calculate the next Fibonacci number
    fib_next = fib1 + fib2

    # Update fib1 and fib2 for the next iteration
    fib1 = fib2
    fib2 = fib_next

    # increment the counter
    count += 1

print(f"The sum of the first 50 Fibonacci numbers is: {sum}")

mean_shirt = mean_color_values(grouped)
mostWornColor = most_worn(grouped)
medianColor = median_color(grouped)

# medianColor = median_color(grouped)
print(
    f'The mean color of shirt is {str(mean_shirt[0])} ,  mostly worn color is {mostWornColor} , median color is {str(medianColor[0])}')
