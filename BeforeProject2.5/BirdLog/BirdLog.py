def main():
	birds = []
	f = open("survey.txt", "r")
	for line in f:
		birds.append(line[:-1].upper())
	print birds

	while True:
		print "Search for a bird (type q to quit):",
		search = raw_input().upper()
		if search == "Q":
			print "Bye!"
			break;
		else:
			if search in birds:
				print search + " is in your bird log :)"
			else:
				print search + " is not in your bird log :("

main()
