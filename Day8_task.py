alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction, original_text, shift_amount):
    new_text = ""
    for char in original_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == "encode":
                position += shift_amount
                if position > 26:
                    position -= 26
            elif direction == "decode":
                position -= shift_amount
                if position < 0:
                    position += 26
            else:
                print("Invalid direction")
            new_text += alphabet[position]
        else:
            new_text += char
    print(new_text)

running = True
while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, direction=direction)

    if input("Continue? (y/n): ").lower() == "n":
        print("Thank you for using Caesar Cipher (From: Marie)")
        running = False
