import random


# Function to shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


# Main program starts here

# Ask the user for the desired password length
password_length = int(
    input("Enter the desired length of the password (8 to 16): "))

# Ensure the length is between 8 and 16
while password_length < 8 or password_length > 16:
  password_length = int(input("Please enter a valid length (8 to 16): "))

# Generate a random mix of characters
uppercaseLetters = [
    chr(random.randint(65, 90)) for _ in range(password_length // 4)
]
lowercaseLetters = [
    chr(random.randint(97, 122)) for _ in range(password_length // 4)
]
numbers = [chr(random.randint(48, 57)) for _ in range(password_length // 4)]
specialChars = [
    chr(random.randint(33, 47)) for _ in range(password_length // 4)
]

# If the password length is not divisible by 4, add extra characters to make up the length
remaining_length = password_length - (len(uppercaseLetters) +
                                      len(lowercaseLetters) + len(numbers) +
                                      len(specialChars))
all_chars = uppercaseLetters + lowercaseLetters + numbers + specialChars

for _ in range(remaining_length):
  all_chars.append(chr(random.randint(
      33, 126)))  # Add random printable ASCII characters

# Generate password using all the characters, in random order
password = ''.join(all_chars)
password = shuffle(password)

# Output
print("Generated password:", password)
