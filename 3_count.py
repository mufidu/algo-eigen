INPUT = ['xc', 'dz', 'bbb', 'dz']
QUERY = ['bbb', 'ac', 'dz']

def count(input, query):
	output = []
	for word in query:
		count = input.count(word)
		output.append(count)
	return output

print(count(INPUT, QUERY))
