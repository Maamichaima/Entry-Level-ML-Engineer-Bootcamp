
kata = {
'Python': 'Guido van Rossum',
'Ruby': 'Yukihiro Matsumoto',
'PHP': 'Rasmus Lerdorf',
}
# print (kata)

for i in kata:
	print(f"{i} was created b {kata[i]}")

print("-------------------------------------")

for language, creator in kata.items():
    print(f"{language} was created by {creator}")