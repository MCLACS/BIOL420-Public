states = {}
states["ME"] = "Maine"
states["MA"] = "Massachusetts"
states["NH"] = "New Hampshire"
states["CT"] = "Connecticut"
states["RI"] = "Rhode Island"
states["VT"] = "Vermont"

def main():
	c = 0
	while c < 6:
		print "Enter the abbreviation for a state in New England:",
		abbr = raw_input()
		if abbr in states:
			print "Good job!  The full name of", abbr, "is", states[abbr]
			del states[abbr]
			c = c+1;
			if c < 6:
				print "You have", 6-c, "more to go!"
			else:
				print "You win!"
		else:
			print "Invalid state or you have entered the state already."

main()
