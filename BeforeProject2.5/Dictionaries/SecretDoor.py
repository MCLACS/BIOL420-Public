def main():
	boxes = {}
	print "You will be asked to hide 5 items in 5 labeled boxes."
	for i in range(0,5):
		print "Enter the label for the box #", i+1,
		label = raw_input()
		print "Enter the name of the item you want to hide in box #", i+1,
		name = raw_input()
		boxes[label] = name
	go = True
	while go:
		print "Enter a box label and I will tell you what is in it (q to quit):",
		label = raw_input()
		if label != 'q':
			if label in boxes:
				print label, "contains", boxes[label]
			else:
				print "Invalid box label"
		else:
			go = False

main()
