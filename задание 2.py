import random
import time

lives = 10

word_wariants = ["dog", "cat", "hamster"]

words_right = random.choice(word_wariants)

word_in_g = "_" * len(words_right)

while ("_" in word_in_g) and (lives > 0):

    print("Lives count:", lives)

    print(word_in_g)

    letter = input("Input character:")

    if letter in words_right:
        print("You are right")
        index = -1
        i = 0
        while i != words_right.count(letter):
            index = words_right.find(letter, index + 1)
            word_in_g = word_in_g[:index:] + letter + word_in_g[(index + 1):]
            i += 1

    else:
        lives -= 1
        print("Try one more time")

if (lives > 0):
    print("You win!")
    print(word_in_g)
else:
    print("You lose:(")
time.sleep(5)
