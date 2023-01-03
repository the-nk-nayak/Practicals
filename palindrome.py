word = input("Check your word for palindrome, Enter the word: - ")
if word == word[::-1]:
    print("This word is Palindrome")
else:
    print(f"The word {word} is not a palindrome")