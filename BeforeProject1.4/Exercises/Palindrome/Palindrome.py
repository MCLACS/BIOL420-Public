def main():
    
    print "Enter a word:",
    word1 = raw_input().upper()
    word2 = ""

    for ch in word1:
        word2 = ch + word2

    if word1 == word2:
        print "You entered a palindrome!"
    else:
        print "You did not enter a palindrome!"

main()
