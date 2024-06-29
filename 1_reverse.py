string = input("Input the string (default=NEGIE1): ")

if string == "":
	string = "NEGIE1"

alphabet = ""
for char in string:
	if char.isalpha():
		alphabet += char
	else:
		break

reverse_alphabet = alphabet[::-1]

result = reverse_alphabet + string[-1]

print(result)
