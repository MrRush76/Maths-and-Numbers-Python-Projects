def credit_card_checker(credit_card):
  # Check if the credit card number length is 16 digits
  if len(credit_card) != 16:
    print("Invalid credit card number")
  else:
    # Iterate over each digit in the credit card number
    for i in range(len(credit_card)):
      # Convert each character to an integer
      credit_card[i] = int(credit_card[i])
      # Double every second digit (starting from the first digit)
      if i % 2 == 0:
        credit_card[i] *= 2
        # If doubling results in a number greater than 9, sum the digits of the product
        if credit_card[i] > 9:
          new_number = [int(d) for d in str(credit_card[i])]
          credit_card[i] = sum(new_number)
    # Check if the sum of all digits is divisible by 10
    if sum(credit_card) % 10 == 0:
      print("Valid credit card number")
    else:
      print("Invalid credit card number")

# Prompt the user to enter their credit card number and convert it to a list of integers
credit_number = list(map(int, input("Enter your credit card number: ")))
credit_card_checker(credit_number)