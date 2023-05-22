import random

# choose a word from list
words_list = ["moving", "people", "computer"]
chosen_word = random.choice(words_list)
# user guess
guess = input("Enter a letter pls: ").lower()
blank_word = []
life = 6
flag = False
for _ in range(len(chosen_word)):
    if chosen_word[_] == guess:
        flag = True
        blank_word += guess
    else:
        blank_word.append("_")
print(blank_word)
flag = False
while "_" in blank_word:
    guess = input("Enter a letter pls: ").lower()
    for letter in range(len(chosen_word)):
        if guess == chosen_word[letter]:
            blank_word[letter] = guess
    print(blank_word)
#end while
print("You won")

