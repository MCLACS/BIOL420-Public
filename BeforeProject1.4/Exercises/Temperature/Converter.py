from Temp import *

def main():

    print "Enter a temp in F:",
    f = float(raw_input())
    print f, "converted to K = ", FtoK(f);
    print f, "converted to C = ", FtoC(f);

    print "Enter a temp in C:",
    c = float(raw_input())
    print c, "converted to K = ", CtoK(c);
    print c, "converted to F = ", CtoF(c);

    print "Enter a temp in K:",
    k = float(raw_input())
    print k, "converted to F = ", KtoF(k);
    print k, "converted to C = ", KtoC(k);

main()
