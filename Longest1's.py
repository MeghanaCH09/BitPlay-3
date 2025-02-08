def longest_consecutive_ones(number):
    binary_representation = bin(number)[2:]
    
    groups_of_ones = binary_representation.split('0')
    
    longest = max(len(group) for group in groups_of_ones)
    
    return longest

number = int(input("Enter a number: "))
result = longest_consecutive_ones(number)
print(f"The longest consecutive 1's in the binary representation of {number} is: {result}")