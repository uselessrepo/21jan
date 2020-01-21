def isVowel(letter):
    if letter[0]=='A' or letter[0] == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
        final = "letter is vowel"
    else:
        final = "letter is consonant"
    return final

letter = input("Enter a letter : ")
isVowels = isVowel(letter)
print(isVowels)