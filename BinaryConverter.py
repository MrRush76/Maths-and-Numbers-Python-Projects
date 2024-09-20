def binary_to_decimal():
  # Initialize decimal result to 0
  decimal = 0
  # Read binary number from user input and convert it to a list of integers
  binary = list(map(int, input("Enter a binary number: ")))
  # Calculate the initial bit length (2^(number of bits - 1))
  bitlength = 2**(len(binary) - 1)
  # Iterate over each bit in the binary number
  for bit in binary:
    # If the bit is 1, add the current bit length to the decimal result
    if bit == 1:
      decimal += bitlength
    # Halve the bit length for the next bit
    bitlength /= 2
  # Print the resulting decimal number
  print(decimal)


def decimal_to_binary():
  # Read decimal number from user input
  decimal = int(input("Enter a decimal number: "))
  # Initialize an empty list to store binary digits
  binary = []
  # Convert decimal to binary
  while decimal > 0:
    # Get the remainder when decimal is divided by 2 (0 or 1)
    remainder = decimal % 2
    # Append the remainder to the binary list
    binary.append(remainder)
    # Update decimal to be the quotient of decimal divided by 2
    decimal = decimal // 2
  # Print the binary number (reversed to get the correct order)
  print("".join(map(str, binary[::-1])))


# Ask the user to choose between binary to decimal or decimal to binary conversion
choice = input("Enter 1 to convert binary to decimal or 2 to convert decimal to binary: ")

# Call the appropriate function based on user choice
if choice == '1':
  binary_to_decimal()
elif choice == '2':
  decimal_to_binary()
else:
  # Print an error message if the choice is invalid
  print("Invalid choice")