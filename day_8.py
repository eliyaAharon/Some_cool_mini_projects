alphabet_list = [chr(i) for i in range(97, 123)]
alphabet_list.extend(chr(i) for i in range(97, 123))
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")

text = input("Type your message: \n").lower()
shift = int(input("Type the shift number: \n"))


def caesar(start_text, shift_amount, ciper_direction):
    end_text = ""
    for letter in start_text:
        if ciper_direction == "encode":
            end_text += alphabet_list[alphabet_list.index(letter) + shift_amount]
        elif ciper_direction == "decode":
            end_text += alphabet_list[alphabet_list.index(letter) - shift_amount]
    print(f"the {ciper_direction} is : {end_text}" )


caesar(text, shift, direction)
