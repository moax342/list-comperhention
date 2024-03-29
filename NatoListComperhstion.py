import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
nato_alphabets={row.letter:row.code for (index, row) in df.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("Enter your name or the name you want").upper()
output = {letter:nato_alphabets[letter] for letter in name}
print(output)
