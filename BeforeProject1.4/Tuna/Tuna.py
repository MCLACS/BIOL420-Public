from Module import *

def main():
    print "Enter the initial tuna population:",
    init = int(raw_input())
    print "Enter the birth rate (fry/(adults*year)):",
    birth = float(raw_input())
    print "Enter the rate of survival of fry (fry/year):",
    survival = float(raw_input())
    print "Enter the natrual death rate (adults/year):",
    death = float(raw_input())
    print "Enter the total harvest (adults/year):",
    harvest = int(raw_input())
    print "Enter the number of years:",
    years = int(raw_input())

    pop = init;
    print "Year\tPopulation"
    for i in range(0, int(years), 1):
        print i, "\t", pop
        fry = calculateFry(pop, birth, survival)
        adultDeath = calculateDeath(pop, death)
        pop = newPopulation(pop, harvest, adultDeath, fry)
    print ""
    print "Final population after", years, "years:", pop

main()
