def main():

    dead = 0
    baby = 0
    adult = 0
    inj = 0

    print "Enter the catch string:",
    data = raw_input()
    data = data.upper()
    for ch in data:
        if ch == 'D':
            dead = dead + 1
        elif ch == 'J':
            baby = baby + 1
        elif ch == 'A':
            adult = adult + 1
        elif ch == 'I':
            inj = inj + 1
        else:
            raise Exception('Error, invalid catch data ' + ch)

    print "Dead\tJuvenile\tAdult\tInjured\tTotal"
    print dead, "\t", baby, "\t\t", adult, "\t", inj, "\t", len(data)

main()
