# +---+---+---+---+---+
# | H | e | l | l | o |
# +---+---+---+---+---+
#   0   1   2   3   4   5
#  -5  -4  -3  -2  -1

def main():
	words = "Purple cows like eating weeds made of cardboard"
	print "The following string is our subject:"
	print words
	print "Lets slice and dice this string!"
	print "Enter the start of the slice (* to leave it out): ",
	start = raw_input()
	print "Enter the end of the slice (* to leave it out): ",
	end = raw_input()
	print "Enter the step of the slice: ",
	step = raw_input()
	print "Purple cows like eating weeds made of cardboard"
	if start == "*" and end == "*":
		print "Sliced with [::"+step+"] " + words[::int(step)]
	elif start == "*":
		print "Sliced with [:"+end+":"+step+"] " + words[:int(end):int(step)]
	elif end == "*":
		print "Sliced with ["+start+"::"+step+"] " + words[int(start)::int(step)]
	else:
		print "Sliced with ["+start+":"+end+":"+step+"] " + words[int(start):int(end):int(step)]


main()
