def main():
		log = {}
		f = open("birdlog.txt", "r")
		for line in f:
			line = line[:-1]
			tokens = line.split(",")
			print tokens
			dt = tokens[0]
			sighting = {}
			sighting["bird"] = tokens[1]
			sighting["count"] = tokens[2]
			sighting["place"] = tokens[3]
			if dt not in log:
				log[dt] = [];
			log[dt].append(sighting)
		while True:
			print "Enter a date ('l' to list dates, 'q' to quit):",
			x = raw_input().upper()
			if (x == 'L'):
				print log.keys()
			elif (x == 'Q'):
				break
			elif x not in log:
				print "Sorry, no sightings on that date."
			else:
				print "There were", len(log[x]), "sightings on that date:"
				for s in log[x]:
					print s["count"], "-", s["bird"], "@", s["place"]

main()
