def main():
	bestX = 0
	bestY = 101
	bestZ = 0
	for x in range(1,100):
		for y in range(1,100):
			for z in range(1,100):
				if 2*x*x - 3*y + 10*z*z + 43 == 0:
					print "Solution: ", x, y, z
					if y < bestY:
						bestX = x
						bestY = y
						bestZ = z
	print "Best Solution: ", bestX, bestY, bestZ


main()
