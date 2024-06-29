string = input("Input the string (default=Saya sangat senang mengerjakan soal algoritma): ")

if string == "":
	string = "Saya sangat senang mengerjakan soal algoritma"

def longest(string):
	words = string.split()	
	longest_word = ""
	for word in words:
		if len(word) > len(longest_word):
			longest_word = word
	return longest_word

print(longest(string))
