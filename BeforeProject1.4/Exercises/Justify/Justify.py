def justify(text):
    spaces = 80 - len(text)
    newText = (' '*spaces) + text
    return newText

def main():
    print "Enter some text:",
    someText = raw_input()
    justified = justify(someText)
    print "01234567890123456789012345678901234567890123456789012345678901234567890123456789"
    print justified

main()
