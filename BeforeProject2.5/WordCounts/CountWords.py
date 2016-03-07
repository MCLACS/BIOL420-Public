def main():
	f = open('24hrs.txt', 'r')
	d = {}
	for line in f:
		line = line[:-1]
		line = line.upper()
		words = line.split()
		for word in words:
			if word in d:
				d[word] = d[word] + 1
			else:
				d[word] = 1

	while True:
		print "Enter a word (q to quit): ",
		w = raw_input().upper()
		if w == "Q":
			break
		elif w in d:
			print w + " appears " + str(d[w]) + " times."
		else:
			print w + " appears 0 times."

main()
