
people_bits = {}
# user bit details
user_name = input("Enter your name: ")
user_bit = input("Enter your bit: ")
people_bits[user_name] = user_bit

another_bit = input("Do you have another bit? 'yes' or 'no' ").lower()

while another_bit == "yes":
    user_name = input("Enter your name: ")
    user_bit = input("Enter your bit: ")
    people_bits[user_name] = user_bit
    another_bit = input("Do you have another bit? 'yes' or 'no' ").lower()

print(f"The winner in the bit is {max(people_bits)} bit of {people_bits[max(people_bits)]}")
