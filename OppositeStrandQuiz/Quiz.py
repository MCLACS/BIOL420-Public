import random

letters = ['A', 'C', 'G', 'T']

def main():
	while True:
		try:
			strand = generateStrand(3)
			correct = opposite(strand)
			opp = getUserInput(strand)
			if (opp == "Q"):
				break
			if opp == correct:
				print "Correct!"
			else:
				print "Incorrect! Answer is", correct
		except Exception as e:
			print "Invlalid DNA strand. Valid nucleotides are A, C, G and T"

def getUserInput(strand):
	print "Enter opposite of", strand, "(Q to Quit): ",
	opp = raw_input();
	for ch in opp:
		if (ch != 'A' and ch != 'C' and ch != 'G' and ch != 'T' and ch != 'Q'):
			raise Exception('Error, invalid nucleotide ' + ch)
	return opp

def generateStrand(len):
	strand = ''
	for i in range(0,len):
		n = random.randint(0,3)
		strand = strand + letters[n]
	return strand

def opposite(strand):
    strand2 = '';
    for ch in strand:
        if ch == 'A':
            strand2 = strand2 + 'T'
        elif ch == 'C':
            strand2 = strand2 + 'G'
        elif ch == 'G':
            strand2 = strand2 + 'C'
        elif ch == 'T':
            strand2 = strand2 + 'A'

    return strand2

main()
