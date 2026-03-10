from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

def caesar(text, shift, direction):
    result = ""
    if direction == "decode":
        shift = -shift

    for char in text:
        if char in alphabet:
            new_index = (alphabet.index(char) + shift) % 26
            result += alphabet[new_index]
        else:
            result += char  # keep spaces, numbers, punctuation as-is

    return result


print(logo)
print("Welcome to the Caesar Cipher!")

while True:
    direction = input("\nType 'encode' to encrypt, 'decode' to decrypt, or 'quit' to exit:\n> ").lower()

    if direction == "quit":
        print("Goodbye!")
        break

    if direction not in ("encode", "decode"):
        print("Invalid option. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n> ").lower()

    while True:
        try:
            shift = int(input("Type the shift number (1-25):\n> "))
            if 1 <= shift <= 25:
                break
            else:
                print("Please enter a number between 1 and 25.")
        except ValueError:
            print("That's not a valid number. Try again.")

    output = caesar(text, shift, direction)
    print(f"\nHere is the {direction}d result: {output}")
