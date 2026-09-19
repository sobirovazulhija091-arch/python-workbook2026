alph = input()
if alph.lower() == 'y':
    print("sometimes vowel, sometimes consonant")
elif alph.lower() in ['a', 'e', 'i', 'o', 'u']:
    print("vowel")
else:
    print("consonant")